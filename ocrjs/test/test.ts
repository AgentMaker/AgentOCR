import fs from 'fs'
import OCR from '../src'
import { base64_to_image } from '@silvia-odwyer/photon-node'

async function main() {
    const ocr = await new OCR().init()
    
    // text direction
    const img1 = readImg(`img/a.png`)
    console.log("text cls up:", await ocr.cls(img1.get_base64()))
    
    // text det
    const img2 = readImg(`img/boarder.png`)
    const points = await ocr.det(img1.get_base64())
    // console.log("text det:", points)

    watermark(img1, img2, points.leftTop.x ,points.leftTop.y)
    watermark(img1, img2, points.rightBottom.x ,points.rightBottom.y)
    watermark(img1, img2, points.leftTop.x ,points.rightBottom.y)
    watermark(img1, img2, points.rightBottom.x ,points.leftTop.y)

    storeImg(img1, "out.png")
    
    // text rec
    // console.log("text rec:", await ocr.rec(imgBase64))
    
    // text ocr [todo]
    // console.log("text ocr:", await ocr.ocr(imgBase64))
}

function readImg(path: string) {
    const imgBase64 = fs.readFileSync(path, { encoding: 'base64' })
    const b_data = imgBase64.replace(/^data:image\/(png|jpg);base64,/, "")
    return base64_to_image(b_data)
}

import { watermark, PhotonImage } from '@silvia-odwyer/photon-node'

function storeImg(img:PhotonImage,name:string) {
    const output_base64 = img.get_base64()
    const output_data = output_base64.replace(/^data:image\/\w+;base64,/, '');
    fs.writeFile(name, output_data, {encoding: 'base64'}, ()=>{});
}

main()