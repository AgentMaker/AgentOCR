import { TypedTensor, Tensor } from 'onnxruntime-common'

export interface Feeds {
    [index: string]: TypedTensor<"float32">
}

export interface Point {
    x: number,
    y: number
}

export type PreInfer = (img: import('@silvia-odwyer/photon').PhotonImage) => typeof img | Promise<typeof img>
export type PostInfer<T> = (tensor: Tensor) => T | Promise<T>