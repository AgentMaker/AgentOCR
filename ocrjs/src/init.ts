
import { InferenceSession } from "onnxruntime-common"

const inWeb = process === undefined

type ModuleType<T extends Promise<any>> = T extends Promise<infer R> ? R : any

const onnxModule =
  (inWeb ? import("onnxruntime-web") : import("onnxruntime-node"))
type onnxModuleType = ModuleType<typeof onnxModule>
const photonModule =
  (inWeb
    ? import("@silvia-odwyer/photon")
    : import("@silvia-odwyer/photon-node"))
type photonModuleType = ModuleType<typeof photonModule>

async function init() {
  const onnxruntime = await onnxModule
  const photon = await photonModule

  return { onnxruntime, photon }
}


export interface ReshapeOption {
    mean?: number[] 
    std?: number[]
    bgr?: boolean
    normalizeType?: number
}

interface InferInput {
  base64: string
  modelSession: InferenceSession
  onnxruntime: onnxModuleType
  photon: photonModuleType,
  reshapeOpt?: ReshapeOption
}

export type { onnxModuleType, photonModuleType, InferInput }
export default init
