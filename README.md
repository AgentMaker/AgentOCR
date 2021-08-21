# AgentOCR
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
    
    * Jupyter Notebook：[【快速使用】](examples/quick_start.ipynb)
    * 更多安装使用细节请参考：[【Package 使用指南】](docs/package_usage.md)

## 多语言支持
* 目前预置了如下语言的配置文件，可通过语言缩写直接调用该配置文件：

    | 语种 | 描述 | 缩写 | | 语种 | 描述 | 缩写 |
    | --- | --- | --- | ---|--- | --- | --- |
    |中文|chinese and english|ch| |保加利亚文|Bulgarian |bg|
    |英文|english|en| |乌克兰文|Ukranian|uk|
    |法文|french|fr| |白俄罗斯文|Belarusian|be|
    |德文|german|german| |泰卢固文|Telugu |te|
    |日文|japan|japan| |阿巴扎文|Abaza |abq|
    |韩文|korean|korean| |泰米尔文|Tamil |ta|
    |中文繁体|chinese traditional |cht| |南非荷兰文 |Afrikaans |af|
    |意大利文| Italian |it| |阿塞拜疆文 |Azerbaijani    |az|
    |西班牙文|Spanish |es| |波斯尼亚文|Bosnian|bs|
    |葡萄牙文| Portuguese|pt| |捷克文|Czech|cs|
    |俄罗斯文|Russia|ru| |威尔士文 |Welsh |cy|
    |阿拉伯文|Arabic|ar| |丹麦文 |Danish|da|
    |印地文|Hindi|hi| |爱沙尼亚文 |Estonian |et|
    |维吾尔|Uyghur|ug| |爱尔兰文 |Irish |ga|
    |波斯文|Persian|fa| |克罗地亚文|Croatian |hr|
    |乌尔都文|Urdu|ur| |匈牙利文|Hungarian |hu|
    |塞尔维亚文（latin)| Serbian(latin) |rs_latin| |印尼文|Indonesian|id|
    |欧西坦文|Occitan |oc| |冰岛文 |Icelandic|is|
    |马拉地文|Marathi|mr| |库尔德文 |Kurdish|ku|
    |尼泊尔文|Nepali|ne| |立陶宛文|Lithuanian |lt|
    |塞尔维亚文（cyrillic)|Serbian(cyrillic)|rs_cyrillic| |拉脱维亚文 |Latvian |lv|
    |毛利文|Maori|mi| | 达尔瓦文|Dargwa |dar|
    |马来文 |Malay|ms| | 因古什文|Ingush |inh|
    |马耳他文 |Maltese |mt| | 拉克文|Lak |lbe|
    |荷兰文 |Dutch |nl| | 莱兹甘文|Lezghian |lez|
    |挪威文 |Norwegian |no| |塔巴萨兰文 |Tabassaran |tab|
    |波兰文|Polish |pl| | 比尔哈文|Bihari |bh|
    | 罗马尼亚文|Romanian |ro| | 迈蒂利文|Maithili |mai|
    | 斯洛伐克文|Slovak |sk| | 昂加文|Angika |ang|
    | 斯洛文尼亚文|Slovenian |sl| | 孟加拉文|Bhojpuri |bho|
    | 阿尔巴尼亚文|Albanian |sq| | 摩揭陀文 |Magahi |mah|
    | 瑞典文|Swedish |sv| | 那格浦尔文|Nagpur |sck|
    | 西瓦希里文|Swahili |sw| | 尼瓦尔文|Newari |new|
    | 塔加洛文|Tagalog |tl| | 保加利亚文 |Goan Konkani|gom|
    | 土耳其文|Turkish |tr| | 沙特阿拉伯文|Saudi Arabia|sa|
    | 乌兹别克文|Uzbek |uz| | 阿瓦尔文|Avar |ava|
    | 越南文|Vietnamese |vi| | 阿瓦尔文|Avar |ava|
    | 蒙古文|Mongolian |mn| | 阿迪赫文|Adyghe |ady|

## 预训练模型
* 检测模型：

    | Model Name | Model Type | Pretrained Model |
    |:-:|:-:|:-:|
    | ch_ppocr_mobile_v2.0_det | det | [Download][ch_ppocr_mobile_v2.0_det] |
    | ch_ppocr_server_v2.0_det | det | [Download][ch_ppocr_server_v2.0_det] |
    | en_ppocr_mobile_v2.0_det | det | [Download][en_ppocr_mobile_v2.0_det] |
    | en_ppocr_mobile_v2.0_table_det | det | [Download][en_ppocr_mobile_v2.0_table_det] |

* 分类模型：

    | Model Name | Model Type | Pretrained Model |
    |:-:|:-:|:-:|
    | ch_ppocr_mobile_v2.0_cls | cls | [Download][ch_ppocr_mobile_v2.0_cls] |

* 识别模型：

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
