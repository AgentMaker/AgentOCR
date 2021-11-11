import { InferInput, ReshapeOption } from "../init";
import { Feeds, PostInfer, PreInfer } from "./types";

export async function infer<T>(
  opt: InferInput,
  postInfer: PostInfer<T>,
  preInfer?: PreInfer,
) {
  const { base64, modelSession, onnxruntime, photon, reshapeOpt = {} } = opt;
  const { Tensor } = onnxruntime;
  const { PhotonImage } = photon;
  const data = base64.replace(/^data:image\/(png|jpg);base64,/, "");
  let phtn_img = PhotonImage.new_from_base64(data);
  if (preInfer !== undefined) phtn_img = await preInfer(phtn_img);
  const width = phtn_img.get_width();
  const height = phtn_img.get_height();
  const img = allReshapeToRGB(phtn_img.get_raw_pixels(), width, height, reshapeOpt);
  try {
    const dims = [1, 3, width, height];
    // 输入模型的数据
    const feeds = <Feeds> {};
    feeds[modelSession.inputNames[0]] = new Tensor("float32", img, dims);
    // 进行模型推理
    const results = await modelSession.run(feeds);
    // 读取结果
    const dataC = results[modelSession.outputNames[0]];

    return await postInfer(dataC);
  } catch (e) {
    throw e;
  }
}

export function yResize(n: number) {
  n = n < 32 ? 32 : n;
  const y = n % 32;
  if ((32 - (2 * y)) > 0) {
    n = n - y;
  } else {
    n = n + 32 - y;
  }
  return n;
}

/**
 * 全部转rgb * H * W
 * @param imageData 数据
 * @param opt 参数
 * @param opt.mean 均值
 * @param opt.std 方差
 */
function allReshapeToRGB(
  imageData: Uint8Array,
  width: number,
  height: number,
  opt: ReshapeOption,
) {
  // mean和std是介于0-1之间的
  const { mean = [0, 0, 0], std = [1, 1, 1], bgr = false, normalizeType = 0 } =
    opt;
  const result = new Float32Array(height * width * 3);
  let offset = 0;
  // h w c
  for (let i = 0; i < height; ++i) {
    const iw = i * width;
    for (let j = 0; j < width; ++j) {
      const iwj = iw + j;
      for (let k = 0; k < 3; ++k) {
        const a = bgr ? iwj * 4 + (2 - k) : iwj * 4 + k;
        result[offset] = normalizeType === 0
          ? imageData[a] / 255
          : (imageData[a] - 128) / 128;
        result[offset] -= mean[k];
        result[offset] /= std[k];
        offset++;
      }
    }
  }
  return result;
}
