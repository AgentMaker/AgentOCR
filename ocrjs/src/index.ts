import { clsInfer, detInfer, recInfer } from "./infer"
import init, { onnxModuleType, photonModuleType } from "./init"
import fetch from "cross-fetch"
import { models } from "./config"
import { InferenceSession } from "onnxruntime-common"

export default class OCR {
  private onnxruntime!: onnxModuleType
  private photon!: photonModuleType
  private models: Map<string, InferenceSession> = new Map();
  constructor() { }

  async init() {
    const { onnxruntime, photon } = await init()
    this.onnxruntime = onnxruntime
    this.photon = photon
    return this
  }

  private async getOrDownLoadModel(modelURL: string) {
    if (!this.models.has(modelURL)) {
      const res = await fetch(modelURL)
      this.models.set(
        modelURL,
        await this.onnxruntime.InferenceSession.create(await res.arrayBuffer()),
      )
    }
    return this.models.get(modelURL) as InferenceSession
  }

  async cls(base64: string) {
    return await clsInfer(
      {
        base64,
        modelSession: await this.getOrDownLoadModel(models.cls.ch_mul_m_cls),
        onnxruntime: this.onnxruntime,
        photon: this.photon,
      },
    )
  }

  // todo 调参 resizemethod
  async det(base64: string) {
    return await detInfer(
      {
        base64,
        modelSession: await this.getOrDownLoadModel(models.det.ch_mul_v2_c_det),
        onnxruntime: this.onnxruntime,
        photon: this.photon,
      }, 1
    )
  }

  // todo 调参 resizemethod
  async rec(base64: string) {
    return await recInfer(
      {
        base64,
        modelSession: await this.getOrDownLoadModel(models.rec.ch_v2_c_rec),
        onnxruntime: this.onnxruntime,
        photon: this.photon,
      }, 1
    )
  }
}
