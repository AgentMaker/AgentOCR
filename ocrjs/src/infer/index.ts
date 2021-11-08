import { Tensor } from "onnxruntime-common";
import { InferInput } from "../init";
import { Point } from "./types";
import { infer, yResize } from "./utils";

// 文本方向分类
async function clsInfer(opt: InferInput) {
  // [x,2]
  const postInfer = (
    dataC: Tensor,
  ) => (dataC.data[0] >= dataC.data[1]
    ? { "direction": "up", "confidence": dataC.data[0] }
    : { "direction": "down", "confidence": dataC.data[1] });

  return await infer(opt, postInfer);
}

// 文本检测
async function detInfer(opt: InferInput, resizeMethod: 1 | 2 | 3 | 4 | 5) {
  opt.reshapeOpt = {
    mean: [0.485, 0.456, 0.406],
    std: [0.229, 0.224, 0.225],
    bgr: true,
  };

  const { photon } = opt;
  const { resize } = photon;

  let wb: number;
  let hb: number;

  // wh 必须为 32 倍数
  const preInfer = (img: import("@silvia-odwyer/photon").PhotonImage) => {
    const raw_w = img.get_width();
    const raw_h = img.get_height();

    const new_w = yResize(raw_w);
    const new_h = yResize(raw_h);

    wb = raw_w / new_w;
    hb = raw_h / new_h;

    return resize(img, new_w, new_h, resizeMethod);
  };

  // [x,1,w,h] 解析结果
  const postInfer = (dataC: Tensor) => {
    // min
    let mx: number | null = null;
    let my: number | null = null;
    // max
    let ax = 0;
    let ay = 0;
    const w = dataC.dims[dataC.dims.length - 2];
    dataC.data.forEach((v, i) => {
      if (v > 0.000001) {
        const point = (i + 1);
        const tmpx = point % w;
        const x = tmpx === 0 ? w : tmpx;
        const y = Math.ceil(point / w);

        if (x > ax) ax = x;
        if (y > ay) ay = y;
        if (mx === null || x < mx ) mx = x;
        if (my === null || y < my ) my = y;
      }
    });
    return {
      leftTop: <Point> {
        x: Math.round(<number><unknown>mx * wb),
        y: Math.round(<number><unknown>mx * hb),
      },
      rightBottom: <Point> {
        x: Math.round(ax * wb),
        y: Math.round(ay * hb),
      },
    };
  };
  return await infer(opt, postInfer, preInfer);
}

// 文本识别
async function recInfer(opt: InferInput, resizeMethod: 1 | 2 | 3 | 4 | 5) {
  const { photon } = opt;
  const { resize } = photon;

  // wh 必须为 32
  const preInfer = (img: import("@silvia-odwyer/photon").PhotonImage) =>
    resize(img, 32, 32, resizeMethod);

  // [x,8,6624] todo 解析结果
  const postInfer = (dataC: Tensor) => JSON.stringify(dataC);

  return await infer(opt, postInfer, preInfer);
}

export { clsInfer, detInfer, recInfer };
