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

## 效果展示
* 多语言 OCR：
    * 中英文

        ![](https://ai-studio-static-online.cdn.bcebos.com/c4c758456cc74d9e997a72a25c47a3a57707b0664ed546819e4d5981ba765b13)

            [[[26.0, 37.0], [301.0, 39.0], [301.0, 72.0], [25.0, 70.0]], ['纯臻营养护发素', 0.971377968788147]]
            [[[27.0, 82.0], [172.0, 82.0], [172.0, 103.0], [27.0, 103.0]], ['产品信息/参数', 0.9922086596488953]]
            [[[28.0, 113.0], [330.0, 113.0], [330.0, 133.0], [28.0, 133.0]], ['45元/每公斤，100公斤起订）', 0.9619097709655762]]
            [[[25.0, 143.0], [283.0, 144.0], [283.0, 164.0], [25.0, 163.0]], ['每瓶22元，1000瓶起订）', 0.9908633828163147]]
            [[[24.0, 177.0], [301.0, 176.0], [301.0, 195.0], [24.0, 196.0]], ['【品牌】：代加工方式/OEMODM', 0.9834667444229126]]
            [[[26.0, 210.0], [232.0, 210.0], [232.0, 227.0], [26.0, 227.0]], ['【品名】：纯臻营养护发素', 0.9786152243614197]]
            [[[24.0, 239.0], [241.0, 237.0], [241.0, 257.0], [25.0, 259.0]], ['【产品编号】：YM-X-3011', 0.9821851849555969]]
            [[[415.0, 241.0], [429.0, 241.0], [429.0, 300.0], [415.0, 300.0]], ['DMOEM', 0.8878258466720581]]
            [[[25.0, 272.0], [180.0, 270.0], [180.0, 288.0], [25.0, 289.0]], ['【净含量】：220ml', 0.9954416155815125]]
            [[[26.0, 304.0], [251.0, 304.0], [251.0, 320.0], [26.0, 320.0]], ['【适用人群】：适合所有肤质', 0.9606326818466187]]
            [[[25.0, 334.0], [342.0, 335.0], [342.0, 352.0], [25.0, 351.0]], ['【主要成分】：鲸蜡硬脂醇、燕麦-葡聚', 0.9720807671546936]]
            [[[27.0, 367.0], [279.0, 367.0], [279.0, 381.0], [27.0, 381.0]], ['糖、椰油酰胺内基甜菜碱、泛醇', 0.8544049859046936]]
            [[[368.0, 370.0], [474.0, 370.0], [474.0, 384.0], [368.0, 384.0]], ['（成品包材）', 0.9908912777900696]]
            [[[27.0, 398.0], [360.0, 398.0], [360.0, 412.0], [27.0, 412.0]], ['（主要功能】：可紧致头发磷层，从而达到', 0.9463475942611694]]
            [[[28.0, 431.0], [369.0, 431.0], [369.0, 444.0], [28.0, 444.0]], ['即时持久改善头发光泽的效果，给十燥的头', 0.9470974802970886]]
            [[[28.0, 460.0], [135.0, 460.0], [135.0, 477.0], [28.0, 477.0]], ['发足够的滋养', 0.997718095779419]]

    * 韩文：

        ![](https://ai-studio-static-online.cdn.bcebos.com/d4f9dd815d024114bd4eee7dca03f7222c135073b01642f3866684b404b75d2a)

            [[[400.0, 518.0], [502.0, 513.0], [504.0, 550.0], [402.0, 555.0]], ['오야야', 0.7852867245674133]]
            [[[156.0, 576.0], [760.0, 559.0], [761.0, 594.0], [157.0, 610.0]], ['내가 잔깐 좋아하는 사람이 생겨서 혼과 공공', 0.8225479125976562]]
            [[[203.0, 636.0], [718.0, 625.0], [718.0, 662.0], [203.0, 672.0]], ['않다가 죽어어릴것안 같아서 여기를 한다', 0.8644148707389832]]
            [[[178.0, 691.0], [709.0, 683.0], [709.0, 717.0], [178.0, 724.0]], ['눈 앞이 아른아른 거리는 잘 생긴 얼굴 자꾸', 0.8839521408081055]]
            [[[225.0, 739.0], [658.0, 738.0], [658.0, 770.0], [225.0, 771.0]], ['귀에 냄도는 크의 측촉한 옥소리 예', 0.8728228211402893]]

* 特色功能 OCR：
    * 中国车牌识别：

        ![](https://ai-studio-static-online.cdn.bcebos.com/568f2a7e0e75407a8bbb429a929c358acc37cf0bd2254a11aba5971d59ff1e67)
        
            [[[[213.0, 239.0], [505.0, 231.0], [507.0, 308.0], [215.0, 316.0]], ['沪AD00806', 0.9884898662567139]]]

        ![](https://ai-studio-static-online.cdn.bcebos.com/7eb3b2e7765c44a290b1931587fc3f407e3eb1b246a04eea9d3d2bc2f07e5c1f)

            [[[[71.0, 190.0], [369.0, 190.0], [369.0, 279.0], [71.0, 279.0]], ['苏E05EV8', 0.9944847822189331]]]
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

## 预设配置选项
* 多语言模型配置：

    | 语言 | 说明 | 缩写 | 字典 | 检测模型 | 分类模型 | 识别模型 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |chinese_simplified|简体中文|ch|[chinese_simplified_dict][chinese_simplified_dict]|[chinese_multilingual_v2_common][chinese_multilingual_v2_common]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[chinese_simplified_v2_common][chinese_simplified_v2_common]|
    |chinese_traditional|繁体中文|cht|[chinese_traditional_dict][chinese_traditional_dict]|[chinese_multilingual_v2_common][chinese_multilingual_v2_common]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[chinese_traditional_mobile][chinese_traditional_mobile]|
    |english|英文|en|[english_dict][english_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[english_mobile][english_mobile]|
    |french|法文|fr|[french_dict][french_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[french_mobile][french_mobile]|
    |german|德文|ger|[german_dict][german_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[german_mobile][german_mobile]|
    |korean|韩文|kr|[korean_dict][korean_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[korean_mobile][korean_mobile]|
    |japanese|日文|jp|[japanese_dict][japanese_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[japanese_mobile][japanese_mobile]|
    |kannada|卡纳达文|ka|[kannada_dict][kannada_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[kannada_mobile][kannada_mobile]|
    |telugu|泰卢固文|te|[telugu_dict][telugu_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[telugu_mobile][telugu_mobile]|
    |tamil|泰米尔文|ta|[tamil_dict][tamil_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[tamil_mobile][tamil_mobile]|
    |latin|拉丁文|la|[latin_dict][latin_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[latin_mobile][latin_mobile]|
    |cyrillic|西里尔文|cy|[cyrillic_dict][cyrillic_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[cyrillic_mobile][cyrillic_mobile]|
    |devanagari|梵文|de|[devanagari_dict][devanagari_dict]|[english_multilingual_mobile][english_multilingual_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[devanagari_mobile][devanagari_mobile]|

* 特色功能模型配置：

    | 功能 | 说明 | 缩写 | 字典 | 检测模型 | 分类模型 | 识别模型 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |chinese_license_plate|中国车牌识别|clp|[chinese_license_plate_dict][chinese_license_plate_dict]|[chinese_license_plate_mobile][chinese_license_plate_mobile]|[chinese_multilingual_mobile][chinese_multilingual_mobile]|[chinese_license_plate_mobile][chinese_license_plate_mobile]

[chinese_simplified_dict]:./agentocr/resources/char_dicts/chinese_simplified_dict.txt
[chinese_traditional_dict]:./agentocr/resources/char_dicts/chinese_traditional_dict.txt
[english_dict]:./agentocr/resources/char_dicts/english_dict.txt
[french_dict]:./agentocr/resources/char_dicts/french_dict.txt
[german_dict]:./agentocr/resources/char_dicts/german_dict.txt
[korean_dict]:./agentocr/resources/char_dicts/korean_dict.txt
[japanese_dict]:./agentocr/resources/char_dicts/japanese_dict.txt
[kannada_dict]:./agentocr/resources/char_dicts/kannada_dict.txt
[telugu_dict]:./agentocr/resources/char_dicts/telugu_dict.txt
[tamil_dict]:./agentocr/resources/char_dicts/tamil_dict.txt
[latin_dict]:./agentocr/resources/char_dicts/latin_dict.txt
[cyrillic_dict]:./agentocr/resources/char_dicts/cyrillic_dict.txt
[devanagari_dict]:./agentocr/resources/char_dicts/devanagari_dict.txt

[chinese_multilingual_v2_common]:./README.md#:~:text=chinese_multilingual_v2_common_v2.0_det
[english_multilingual_mobile]:./README.md#:~:text=english_multilingual_mobile_v2.0_det
[chinese_multilingual_mobile]:./README.md#:~:text=chinese_multilingual_mobile_v2.0_cls
[chinese_simplified_v2_common]:./README.md#:~:text=chinese_simplified_v2_common_v2.0_rec
[chinese_traditional_mobile]:./README.md#:~:text=chinese_traditional_mobile_v2.0_rec
[english_mobile]:./README.md#:~:text=english_mobile_v2.0_rec
[french_mobile]:./README.md#:~:text=french_mobile_v2.0_rec
[german_mobile]:./README.md#:~:text=german_mobile_v2.0_rec
[korean_mobile]:./README.md#:~:text=korean_mobile_v2.0_rec
[japanese_mobile]:./README.md#:~:text=japanese_mobile_v2.0_rec
[kannada_mobile]:./README.md#:~:text=kannada_mobile_v2.0_rec
[telugu_mobile]:./README.md#:~:text=telugu_mobile_v2.0_rec
[tamil_mobile]:./README.md#:~:text=tamil_mobile_v2.0_rec
[latin_mobile]:./README.md#:~:text=latin_mobile_v2.0_rec
[cyrillic_mobile]:./README.md#:~:text=cyrillic_mobile_v2.0_rec
[devanagari_mobile]:./README.md#:~:text=devanagari_mobile_v2.0_rec


[chinese_license_plate_dict]:./agentocr/resources/char_dicts/chinese_license_plate_dict.txt

[chinese_license_plate_mobile]:./README.md#:~:text=chinese_license_plate_mobile_v2.0_det
[chinese_license_plate_mobile]:./README.md#:~:text=chinese_license_plate_mobile_v2.0_rec

## 预训练模型
* 常规模型列表：

    | 模型名称 | 类型 | 预训练模型 | 说明 |
    |:-:|:-:|:-:|:-:|
    | chinese_multilingual_mobile_v2.0_det | det | [Download][chinese_multilingual_mobile_v2.0_det] |移动端中文（多语言）文本位置检测模型|
    | chinese_multilingual_server_v2.0_det | det | [Download][chinese_multilingual_server_v2.0_det] |服务端中文（多语言）文本位置检测模型|
    | chinese_multilingual_v2_common_v2.0_det | det | [Download][chinese_multilingual_v2_common_v2.0_det] |V2 版本通用中文（多语言）文本位置检测模型|
    | english_multilingual_mobile_v2.0_det | det | [Download][english_multilingual_mobile_v2.0_det] |移动端英文（多语言）文本位置检测模型|
    | chinese_multilingual_mobile_v2.0_cls | cls | [Download][chinese_multilingual_mobile_v2.0_cls] |移动端中文（多语言）文本方向分类模型|
    | chinese_simplified_mobile_v2.0_rec | rec | [Download][chinese_simplified_mobile_v2.0_rec] |移动端简体中文文本内容识别模型|
    | chinese_simplified_server_v2.0_rec | rec | [Download][chinese_simplified_server_v2.0_rec] |服务端简体中文文本内容识别模型|
    | chinese_simplified_v2_common_v2.0_rec | rec | [Download][chinese_simplified_v2_common_v2.0_rec] |V2 版本通用简体中文文本内容识别模型|
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

* 特色功能模型列表：

    | 模型名称 | 类型 | 预训练模型 | 说明 |
    |:-:|:-:|:-:|:-:|
    | chinese_license_plate_mobile_v2.0_det | det | [Download][chinese_license_plate_mobile_v2.0_det] |移动端中国车牌文本位置检测模型（支持蓝色/绿色单层车牌）|
    | chinese_license_plate_mobile_v2.0_rec | rec | [Download][chinese_license_plate_mobile_v2.0_rec] |移动端中国车牌文本内容识别模型|
    | chinese_license_plate_server_v2.0_rec | rec | [Download][chinese_license_plate_server_v2.0_rec] |服务端中国车牌文本内容识别模型|


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


[chinese_license_plate_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/e06c2624609843e69a0b8f231aa09e5108d406e653f643d2b9d524bdc95f2263?responseContentDisposition=attachment%3B%20filename%3Dchinese_license_plate_mobile_v2.0_det.onnx
[chinese_license_plate_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/16714ee6aa514e1eaa6946dc0189f87d90f168e51db54696bc9cc51002881ce7?responseContentDisposition=attachment%3B%20filename%3Dchinese_license_plate_mobile_v2.0_rec.onnx
[chinese_license_plate_server_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/df3afb41fa244b3d90b59d95a47dc53ba3313fe42c0a438ba8c227ee9e56a699?responseContentDisposition=attachment%3B%20filename%3Dchinese_license_plate_server_v2.0_rec.onnx


[chinese_simplified_v2_common_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/e199a08f2d884261975f7181da69910cad353121666e4dcf931ecb4e59bf83db?responseContentDisposition=attachment%3B%20filename%3Dchinese_simplified_v2_common_v2.0_rec.onnx
[chinese_multilingual_v2_common_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/cddca5cc473f47b9b9405161cf03d0d20b83f96b0f784828bbe98833d01a925a?responseContentDisposition=attachment%3B%20filename%3Dchinese_multilingual_v2_common_v2.0_det.onnx
