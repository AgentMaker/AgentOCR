English | [简体中文](./README.md)

# AgentOCR
![GitHub forks](https://img.shields.io/github/forks/AgentMaker/AgentOCR)
![GitHub Repo stars](https://img.shields.io/github/stars/AgentMaker/AgentOCR)
![Pypi Downloads](https://pepy.tech/badge/agentocr)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/AgentMaker/AgentOCR?include_prereleases)
![GitHub](https://img.shields.io/github/license/AgentMaker/AgentOCR)  

![Test](https://github.com/AgentMaker/AgentOCR/actions/workflows/test.yml/badge.svg?branch=main)
![Build](https://github.com/AgentMaker/AgentOCR/actions/workflows/build.yml/badge.svg?branch=main)

## Introduction
* AgentOCR is an OCR project based on [PaddleOCR][PaddleOCR] and [ONNXRuntime][ONNXRuntime], which is simple to use and convenient to call

* AgentOCR currently contains Python Package **【AgentOCR】** and OCR marking software called [**【AgentOCRLabeling】**](labeling/)

[PaddleOCR]:https://github.com/PaddlePaddle/PaddleOCR
[ONNXRuntime]:https://github.com/microsoft/onnxruntime

## Quick Start
* Python Package：

    * Quick Install：

        ```shell
        # Install AgentOCR
        $ pip install agentocr 
        
        # Install the appropriate ONNXRuntime's version according to the device platform
        $ pip install onnxruntime
        ```

    * Easy Call：

        ```python
        # Import OCRSystem
        from agentocr import OCRSystem

        # Initialize OCR model
        ocr = OCRSystem(config='ch')

        # OCR Detection
        results = ocr.ocr('test.jpg')
        ```
    * Use in Server：

        * Start AgentOCR Server

            ```shell
            $ agentocr server
            ```

        * Easy Call

            ```python
            import cv2
            import json
            import base64
            import requests

            # Encode Picture with Base64
            def cv2_to_base64(image):
                data = cv2.imencode('.jpg', image)[1]
                image_base64 = base64.b64encode(data.tobytes()).decode('UTF-8')
                return image_base64


            # Read Picture
            image = cv2.imread('test.jpg')
            image_base64 = cv2_to_base64(image)

            # Build Request
            data = {
                'image': image_base64
            }

            # Send Request
            url = "http://127.0.0.1:5000/ocr"
            r = requests.post(url=url, data=json.dumps(data))

            # Print Result
            print(r.json())
            ```


    * Jupyter Notebook：[【Quick Start】](examples/quick_start.ipynb)
    * More details, please refer to：[【Package Guide Books】](docs/package_usage.md)

## Multi-Language Support
* The supporting language is as follows. You can directly use it by the language abbreviation：

    | Language | Abbreviation | | Language | Abbreviation |
    | --- | --- | --- | --- | --- |
    |chinese and english|ch| |Bulgarian |bg|
    |english|en| |Ukranian|uk|
    |french|fr| |Belarusian|be|
    |german|german| |Telugu |te|
    |japan|japan| |Abaza |abq|
    |korean|korean| |Tamil |ta|
    |chinese traditional |cht| |Afrikaans |af|
    | Italian |it| |Azerbaijani|az|
    |Spanish |es| |Bosnian|bs|
    | Portuguese|pt| |Czech|cs|
    |Russia|ru| |Welsh |cy|
    |Arabic|ar| |Danish|da|
    |Hindi|hi| |Estonian |et|
    |Uyghur|ug| |Irish |ga|
    |Persian|fa| |Croatian |hr|
    |Urdu|ur| |Hungarian |hu|
    | Serbian(latin) |rs_latin| |Indonesian|id|
    |Occitan |oc| |Icelandic|is|
    |Marathi|mr| |Kurdish|ku|
    |Nepali|ne| |Lithuanian |lt|
    |Serbian(cyrillic)|rs_cyrillic| |Latvian |lv|
    |Maori|mi| |Dargwa |dar|
    |alay|ms| |Ingush |inh|
    |Maltese |mt| |Lak |lbe|
    |Dutch |nl| |Lezghian |lez|
    |Norwegian |no| |Tabassaran |tab|
    |Polish |pl| |Bihari |bh|
    |Romanian |ro| |Maithili |mai|
    |Slovak |sk| |Angika |ang|
    |Slovenian |sl| |Bhojpuri |bho|
    |Albanian |sq| |Magahi |mah|
    |Swedish |sv| |Nagpur |sck|
    |Swahili |sw| |Newari |new|
    |Tagalog |tl| |Goan Konkani|gom|
    |Turkish |tr| |Saudi Arabia|sa|
    |Uzbek |uz| |Avar |ava|
    |Vietnamese |vi| |Avar |ava|
    |Mongolian |mn| |Adyghe |ady|

## Pre-Model
* Detection Model：

    | Model Name | Model Type | Pretrained Model |
    |:-:|:-:|:-:|
    | ch_ppocr_mobile_v2.0_det | det | [Download][ch_ppocr_mobile_v2.0_det] |
    | ch_ppocr_server_v2.0_det | det | [Download][ch_ppocr_server_v2.0_det] |
    | en_ppocr_mobile_v2.0_det | det | [Download][en_ppocr_mobile_v2.0_det] |
    | en_ppocr_mobile_v2.0_table_det | det | [Download][en_ppocr_mobile_v2.0_table_det] |

* Classification Model：

    | Model Name | Model Type | Pretrained Model |
    |:-:|:-:|:-:|
    | ch_ppocr_mobile_v2.0_cls | cls | [Download][ch_ppocr_mobile_v2.0_cls] |

* Identification Model：

    | Model Name | Model Type | Pretrained Model |
    |:-:|:-:|:-:|
    | ch_ppocr_mobile_v2.0_rec | rec | [Download][ch_ppocr_mobile_v2.0_rec] |
    | ch_ppocr_server_v2.0_rec | rec | [Download][ch_ppocr_server_v2.0_rec] |
    | ka_ppocr_mobile_v2.0_rec | rec | [Download][ka_ppocr_mobile_v2.0_rec] |
    | te_ppocr_mobile_v2.0_rec | rec | [Download][te_ppocr_mobile_v2.0_rec] |
    | ta_ppocr_mobile_v2.0_rec | rec | [Download][ta_ppocr_mobile_v2.0_rec] |
    | cht_ppocr_mobile_v2.0_rec | rec | [Download][cht_ppocr_mobile_v2.0_rec] |
    | japan_ppocr_mobile_v2.0_rec | rec | [Download][japan_ppocr_mobile_v2.0_rec] |
    | latin_ppocr_mobile_v2.0_rec | rec | [Download][latin_ppocr_mobile_v2.0_rec] |
    | arabic_ppocr_mobile_v2.0_rec | rec | [Download][arabic_ppocr_mobile_v2.0_rec] |
    | korean_ppocr_mobile_v2.0_rec | rec | [Download][korean_ppocr_mobile_v2.0_rec] |
    | french_ppocr_mobile_v2.0_rec | rec | [Download][french_ppocr_mobile_v2.0_rec] |
    | german_ppocr_mobile_v2.0_rec | rec | [Download][german_ppocr_mobile_v2.0_rec] |
    | cyrillic_ppocr_mobile_v2.0_rec | rec | [Download][cyrillic_ppocr_mobile_v2.0_rec] |
    | en_ppocr_mobile_v2.0_table_rec | rec | [Download][en_ppocr_mobile_v2.0_table_rec] |
    | en_ppocr_mobile_v2.0_number_rec | rec | [Download][en_ppocr_mobile_v2.0_number_rec] |
    | devanagari_ppocr_mobile_v2.0_rec | rec | [Download][devanagari_ppocr_mobile_v2.0_rec] |




[ch_ppocr_mobile_v2.0_cls]:https://bj.bcebos.com/v1/ai-studio-online/0c29ed105d984b7bba9c09ecb6dcde7075330fd74fa7449fafca316603e1aaed?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_cls.onnx

[ch_ppocr_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/55d7b7e1890c4b81ae17a2d0c4b457d89f47a05407be4563a5b2e212b3fdf70b?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_det.onnx
[ch_ppocr_server_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/65e5a792fa464c2994814b0a2af2334ada2a9c8150fa42f6ab3cfd22bb744708?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_server_v2.0_det.onnx
[en_ppocr_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/e02ba8dfb2b34febb9c468114031ca7f4a6e320359a14f5aaa4067b66c3d99bf?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_det.onnx
[en_ppocr_mobile_v2.0_table_det]:https://bj.bcebos.com/v1/ai-studio-online/d28ba772eb1d48a582a7ce16894885d662399f1ee12a4bfaa73d2b4987c3dc31?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_table_det.onnx

[ch_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/77e67a9bb1cc421a97e037462838f159526b2d0ba3d94a3eb0da35408174edb7?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_rec.onnx
[ch_ppocr_server_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/5f6546d18a84448486abe778b9f1b1ba21da2efbd6b84aaa808936e94771ec68?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_server_v2.0_rec.onnx
[ka_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/85cdc2462b6f4ff3a3474b724a33308112b3c55d9bf541469b858b0b0035872c?responseContentDisposition=attachment%3B%20filename%3Dka_mobile_v2.0_rec.onnx
[te_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/a6d61a705348461b93821b963769ddb56502e57bdc47470d9e8c7ed29f80c016?responseContentDisposition=attachment%3B%20filename%3Dte_mobile_v2.0_rec.onnx
[ta_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/ef955098816b47be82538a9fff2487516a8a5da3ec454b689406e01b4031fd41?responseContentDisposition=attachment%3B%20filename%3Dta_mobile_v2.0_rec.onnx
[cht_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/85d2cfd9c24e47319ebb48184f4e8ed3cdef007a8731476eb8efbd3d7b4f5ff9?responseContentDisposition=attachment%3B%20filename%3Dchinese_cht_mobile_v2.0_rec.onnx
[japan_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/df453e13ad144138978ac3d121b5ec73adfccd9a014e4d1281fe9a4015e2cf92?responseContentDisposition=attachment%3B%20filename%3Djapan_mobile_v2.0_rec.onnx
[latin_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/159e47bf6fab45efbe786dc4d932cd71d28f74b0bf9e4144b82f00ebd1a467a5?responseContentDisposition=attachment%3B%20filename%3Dlatin_ppocr_mobile_v2.0_rec.onnx
[arabic_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/27521b051c96454eb10f13f403ca699a819d997e6d2d4afa9721f2f80ad3aed7?responseContentDisposition=attachment%3B%20filename%3Darabic_ppocr_mobile_v2.0_rec.onnx
[korean_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/20d94b1440654ed9aadbe61b565430702629de85021a4e14ad644fae5896ed77?responseContentDisposition=attachment%3B%20filename%3Dkorean_mobile_v2.0_rec.onnx
[french_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/cdc0503a71274172b0d43e07a7c285745231381b52d34be584babe1e1202a9d9?responseContentDisposition=attachment%3B%20filename%3Dfrench_mobile_v2.0_rec.onnx
[german_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/87356bfc558f481fbeaae6fa28b6ea50194c2ae94f4d4165a95927dd9ad4d669?responseContentDisposition=attachment%3B%20filename%3Dgerman_mobile_v2.0_rec.onnx
[cyrillic_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/3f3b53e4b2b74cedaa24b4998e35d4b1c527cc7eb3f645859695de80bb14b625?responseContentDisposition=attachment%3B%20filename%3Dcyrillic_ppocr_mobile_v2.0_rec.onnx
[en_ppocr_mobile_v2.0_table_rec]:https://bj.bcebos.com/v1/ai-studio-online/c9d6e42c99fe40ae9448ee9d07973d2b603f1e68fffa4a29b8f8cc45b3dc16f5?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_table_rec.onnx
[en_ppocr_mobile_v2.0_number_rec]:https://bj.bcebos.com/v1/ai-studio-online/a31fc2aed28841b4ac861c7ae4639d3f62b102d7f5e0416088544a9763affeec?responseContentDisposition=attachment%3B%20filename%3Den_number_mobile_v2.0_rec.onnx
[devanagari_ppocr_mobile_v2.0_rec]:https://bj.bcebos.com/v1/ai-studio-online/a78a9384579d451988858aa97e99d4cc2518902128174b089fabac2a150c8822?responseContentDisposition=attachment%3B%20filename%3Ddevanagari_ppocr_mobile_v2.0_rec.onnx
