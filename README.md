# AgentOCR


```
                                      _      ____     _____   _____  
       /\                            | |    / __ \   / ____| |  __ \ 
      /  \      __ _    ___   _ __   | |_  | |  | | | |      | |__) |
     / /\ \    / _` |  / _ \ | '_ \  | __| | |  | | | |      |  _  / 
    / ____ \  | (_| | |  __/ | | | | | |_  | |__| | | |____  | | \ \ 
   /_/    \_\  \__, |  \___| |_| |_|  \__|  \____/   \_____| |_|  \_\
                __/ |                                                
               |___/                                                                                              
```

![GitHub forks](https://img.shields.io/github/forks/AgentMaker/AgentOCR)
![GitHub Repo stars](https://img.shields.io/github/stars/AgentMaker/AgentOCR)
![Pypi Downloads](https://pepy.tech/badge/agentocr)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/AgentMaker/AgentOCR?include_prereleases)
![GitHub](https://img.shields.io/github/license/AgentMaker/AgentOCR)  

![Test](https://github.com/AgentMaker/AgentOCR/actions/workflows/test.yml/badge.svg?branch=main)
![Build](https://github.com/AgentMaker/AgentOCR/actions/workflows/build.yml/badge.svg?branch=main)

## 简介
* AgentOCR 是一个基于 [PaddleOCR][PaddleOCR] 和 [ONNXRuntime][ONNXRuntime] 项目开发的一个使用简单、调用方便的 OCR 项目

* 本项目目前包含 Python Package **【AgentOCR】** 和 OCR 标注软件 [**【AgentOCRLabeling】**](labeling/)

[PaddleOCR]:https://github.com/PaddlePaddle/PaddleOCR
[ONNXRuntime]:https://github.com/microsoft/onnxruntime

## 使用指南
* Python Package：

    * 快速安装：

        ```shell
        # 安装 AgentOCR
        $ pip install agentocr 
        
        # 根据设备平台安装合适版本的 ONNXRuntime
        $ pip install onnxruntime
        ```

    * 简单调用：

        ```python
        # 导入 OCRSystem 模块
        from agentocr import OCRSystem

        # 初始化 OCR 模型
        ocr = OCRSystem(config='ch')

        # 使用模型对图像进行 OCR 识别
        results = ocr.ocr('test.jpg')
        ```
    * 服务器部署：

        * 启动 AgentOCR Server 服务

            ```shell
            $ agentocr server
            ```

        * Python 调用

            ```python
            import cv2
            import json
            import base64
            import requests

            # 图片 Base64 编码
            def cv2_to_base64(image):
                data = cv2.imencode('.jpg image)[1]
                image_base64 = base64.b64encode(data.tobytes()).decode('UTF-8')
                return image_base64


            # 读取图片
            image = cv2.imread('test.jpg')
            image_base64 = cv2_to_base64(image)

            # 构建请求数据
            data = {
                'image': image_base64
            }

            # 发送请求
            url = "http://127.0.0.1:5000/ocr"
            r = requests.post(url=url, data=json.dumps(data))

            # 打印预测结果
            print(r.json())
            ```


    * Jupyter Notebook：[【快速使用】](examples/quick_start.ipynb)
    * 更多安装使用细节请参考：[【Package 使用指南】](docs/package_usage.md)

## 多语言支持
* 目前预置了如下语言的配置文件，可通过语言缩写直接调用该配置文件：

    | 语言 | 说明 | 缩写 | 字典 |
    |:-:|:-:|:-:|:-:|
    |chinese_simplified|简体中文|ch|[Link](./agentocr/resources/char_dicts/chinese_simplified_dict.txt)|
    |chinese_traditional|繁体中文|cht|[Link](./agentocr/resources/char_dicts/chinese_traditional_dict.txt)|
    |english|英文|en|[Link](./agentocr/resources/char_dicts/english_dict.txt)|
    |french|法文|fr|[Link](./agentocr/resources/char_dicts/french_dict.txt)|
    |german|德文|ger|[Link](./agentocr/resources/char_dicts/german_dict.txt)|
    |korean|韩文|kr|[Link](./agentocr/resources/char_dicts/korean_dict.txt)|
    |japanese|日文|jp|[Link](./agentocr/resources/char_dicts/japanese_dict.txt)|
    |kannada|卡纳达文|ka|[Link](./agentocr/resources/char_dicts/kannada_dict.txt)|
    |telugu|泰卢固文|te|[Link](./agentocr/resources/char_dicts/telugu_dict.txt)|
    |tamil|泰米尔文|ta|[Link](./agentocr/resources/char_dicts/tamil_dict.txt)|
    |latin|拉丁文|la|[Link](./agentocr/resources/char_dicts/latin_dict.txt)|
    |cyrillic|西里尔文|cy|[Link](./agentocr/resources/char_dicts/cyrillic_dict.txt)|
    |devanagari|梵文|de|[Link](./agentocr/resources/char_dicts/devanagari_dict.txt)|



## 预训练模型
* 模型列表：

    | 模型名称 | 类型 | 预训练模型 | 说明 |
    |:-:|:-:|:-:|:-:|
    | chinese_multilingual_mobile_v2.0_det | det | [Download][chinese_multilingual_mobile_v2.0_det] |移动端中文（多语言）文本位置检测模型|
    | chinese_multilingual_server_v2.0_det | det | [Download][chinese_multilingual_server_v2.0_det] |服务端中文（多语言）文本位置检测模型|
    | english_multilingual_mobile_v2.0_det | det | [Download][english_multilingual_mobile_v2.0_det] |移动端英文（多语言）文本位置检测模型|
    | chinese_multilingual_mobile_v2.0_cls | cls | [Download][chinese_multilingual_mobile_v2.0_cls] |移动端中文（多语言）文本方向分类模型|
    | chinese_simplified_mobile_v2.0_rec | rec | [Download][chinese_simplified_mobile_v2.0_rec] |移动端简体中文文本内容识别模型|
    | chinese_simplified_server_v2.0_rec | rec | [Download][chinese_simplified_server_v2.0_rec] |服务端简体中文文本内容识别模型|
    | chinese_traditional_mobile_v2.0_rec | rec | [Download][chinese_traditional_mobile_v2.0_rec] |移动端繁体中文文本内容识别模型|
    | english_mobile_v2.0_rec | rec | [Download][english_mobile_v2.0_rec] |移动端英文文本内容识别模型|
    | korean_mobile_v2.0_rec | rec | [Download][korean_mobile_v2.0_rec] |移动端韩文文本内容识别模型|
    | french_mobile_v2.0_rec | rec | [Download][french_mobile_v2.0_rec] |移动端法文文本内容识别模型|
    | german_mobile_v2.0_rec | rec | [Download][german_mobile_v2.0_rec] |移动端德文文本内容识别模型|
    | japanese_mobile_v2.0_rec | rec | [Download][japanese_mobile_v2.0_rec] |移动端日文文本内容识别模型|
    | telugu_mobile_v2.0_rec | rec | [Download][telugu_mobile_v2.0_rec] |移动端泰卢固文文本内容识别模型|
    | tamil_mobile_v2.0_rec | rec | [Download][tamil_mobile_v2.0_rec] |移动端泰米尔文文本内容识别模型|
    | latin_mobile_v2.0_rec | rec | [Download][latin_mobile_v2.0_rec] |移动端拉丁文文本内容识别模型|
    | arabic_mobile_v2.0_rec | rec | [Download][arabic_mobile_v2.0_rec] |移动端阿拉伯文文本内容识别模型|
    | cyrillic_mobile_v2.0_rec | rec | [Download][cyrillic_mobile_v2.0_rec] |移动端西里尔文文本内容识别模型|
    | kannada_mobile_v2.0_rec | rec | [Download][kannada_mobile_v2.0_rec] |移动端卡纳达文文本内容识别模型|
    | devanagari_mobile_v2.0_rec | rec | [Download][devanagari_mobile_v2.0_rec] |移动端梵文文本内容识别模型|




[chinese_multilingual_mobile_v2.0_cls]:https://bj.bcebos.com/v1/ai-studio-online/71ac2df69f8b41f3be5ea646a3df985b36b96f0494634056bae1305d22e8eedd?responseContentDisposition=attachment%3B%20filename%3Dchinese_multilingual_mobile_v2.0_cls.onnx
[chinese_multilingual_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/6a97ec7f4a2348749887988071733bef674546f8ad7049b79bf3597c8bf9b5a1?responseContentDisposition=attachment%3B%20filename%3Dchinese_multilingual_mobile_v2.0_det.onnx
[chinese_multilingual_server_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/a4efe143749e49039f15448ea8c73d99c0534997a54d4d018bc6bec19c518a37?responseContentDisposition=attachment%3B%20filename%3Dchinese_multilingual_server_v2.0_det.onnx
[english_multilingual_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/90c32bb78fe34870bf3ed7c8d8fdf1a4897abfd42d984a678c865cd92b25b91d?responseContentDisposition=attachment%3B%20filename%3Denglish_multilingual_mobile_v2.0_det.onnx
[chinese_simplified_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/6ae9a6f87f3d4126aab5a92b4df35359bce2159e177a4ed6b2c85a38f9987004?responseContentDisposition=attachment%3B%20filename%3Dchinese_simplified_mobile_v2.0_rec.onnx
[chinese_simplified_server_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/bd641ce2efe842f6a0c53a502c8595ab4121051b66d748ff8cbe555d41ee3c2d?responseContentDisposition=attachment%3B%20filename%3Dchinese_simplified_server_v2.0_rec.onnx
[chinese_traditional_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/1733802270dd42e7b1535a954dad0373cf03b73a0fc14fa5b4f44aa5ecceb351?responseContentDisposition=attachment%3B%20filename%3Dchinese_traditional_mobile_v2.0_rec.onnx
[kannada_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/e26c16c208d64af9840a5c8fd721d5edbaf86dbbbb2c4c5397839d6d078933d4?responseContentDisposition=attachment%3B%20filename%3Dkannada_mobile_v2.0_rec.onnx
[telugu_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/8b85b803a2364f0e9238683b6c8032922ac30cbec4774a1795183195bd717bad?responseContentDisposition=attachment%3B%20filename%3Dtelugu_mobile_v2.0_rec.onnx
[tamil_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/0dc7fc1b438d4ed6ab401b596dcc1407101b9143d9c54d7db6a6ec032cc7f3d2?responseContentDisposition=attachment%3B%20filename%3Dtamil_mobile_v2.0_rec.onnx
[japanese_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/ff50e398096d48889f154910a085af1f170d95d18eac4d6885ad8d1c9f2010f8?responseContentDisposition=attachment%3B%20filename%3Djapanese_mobile_v2.0_rec.onnx
[latin_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/d24e03a0022a4de4805a6e2b60b6a74ad09b2f6ec4cd4397a301048bae4e8a09?responseContentDisposition=attachment%3B%20filename%3Dlatin_mobile_v2.0_rec.onnx
[arabic_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/ea236583c3074d858025f2c5fb9bf01ed45f8416e78146639c40585397eea954?responseContentDisposition=attachment%3B%20filename%3Darabic_mobile_v2.0_rec.onnx
[korean_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/f6d69c38fe9a46569403acf6a1d8cbe5451ed51ad2e64fb2bc9743848fd6f91d?responseContentDisposition=attachment%3B%20filename%3Dkorean_mobile_v2.0_rec.onnx
[french_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/e2ebf93ff016446189e7ad23a988ccaf94d54c883315485f923cc2c555693459?responseContentDisposition=attachment%3B%20filename%3Dfrench_mobile_v2.0_rec.onnx
[german_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/74b5039facea46329ebdfb9f4cd366c8a38b16ed0eac44c190bc9597e7795a56?responseContentDisposition=attachment%3B%20filename%3Dgerman_mobile_v2.0_rec.onnx
[cyrillic_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/4137cfd82c334f4094cae36884478e38ce16416e97eb4dc9a95a192ee70ac42c?responseContentDisposition=attachment%3B%20filename%3Dcyrillic_mobile_v2.0_rec.onnx
[english_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/46da49d9b0ff4da4a8788c31d73029f4bfd132d0cedb4fd3893e40ddadc15d04?responseContentDisposition=attachment%3B%20filename%3Denglish_mobile_v2.0_rec.onnx
[devanagari_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/634d1c1635e5492aac93b195d3b57e5d5013815ea2684d8e96b75d3838bc76b0?responseContentDisposition=attachment%3B%20filename%3Ddevanagari_mobile_v2.0_rec.onnx
