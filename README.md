# AgentOCR
## 简介
* AgentOCR 是一个基于 PaddleOCR 和 ONNXRuntime 项目开发的跨平台、易部署的 OCR 项目

* 支持 PaddleOCR 的多语言预训练模型，以及 PaddleOCR 训练导出的其他模型

## 安装
* pip 安装：

    ```shell
    $ pip install agentocr
    ```

* 源码安装：

    ```shell
    $ git clone https://github.com/AgentMaker/AgentOCR
    $ cd AgentOCR && python setup.py install
    ```

## 使用指南
* 快速使用：

    ```python
    from agentocr import OCRSystem

    ocr = OCRSystem(config_path='config.json')

    results = ocr('test.jpg')
    ```

## 预训练模型

| Model Name | Model Type | Pretrained Model |
|:-:|:-:|:-:|
| ch_ppocr_mobile_v2.0_cls | cls | [Download](ch_ppocr_mobile_v2.0_cls) |
| ch_ppocr_mobile_v2.0_det | det | [Download](ch_ppocr_mobile_v2.0_det) |
| ch_ppocr_server_v2.0_det | det | [Download](ch_ppocr_server_v2.0_det) |
| en_ppocr_mobile_v2.0_table_det | det | [Download](en_ppocr_mobile_v2.0_table_det) |
| ch_ppocr_mobile_v2.0_rec | rec | [Download](ch_ppocr_mobile_v2.0_rec) |
| ch_ppocr_server_v2.0_rec | rec | [Download](ch_ppocr_server_v2.0_rec) |
| ka_ppocr_mobile_v2.0_rec | rec | [Download](ka_ppocr_mobile_v2.0_rec) |
| te_ppocr_mobile_v2.0_rec | rec | [Download](te_ppocr_mobile_v2.0_rec) |
| ta_ppocr_mobile_v2.0_rec | rec | [Download](ta_ppocr_mobile_v2.0_rec) |
| cht_ppocr_mobile_v2.0_rec | rec | [Download](cht_ppocr_mobile_v2.0_rec) |
| japan_ppocr_mobile_v2.0_rec | rec | [Download](japan_ppocr_mobile_v2.0_rec) |
| latin_ppocr_mobile_v2.0_rec | rec | [Download](latin_ppocr_mobile_v2.0_rec) |
| arabic_ppocr_mobile_v2.0_rec | rec | [Download](arabic_ppocr_mobile_v2.0_rec) |
| korean_ppocr_mobile_v2.0_rec | rec | [Download](korean_ppocr_mobile_v2.0_rec) |
| french_ppocr_mobile_v2.0_rec | rec | [Download](french_ppocr_mobile_v2.0_rec) |
| german_ppocr_mobile_v2.0_rec | rec | [Download](german_ppocr_mobile_v2.0_rec) |
| cyrillic_ppocr_mobile_v2.0_rec | rec | [Download](cyrillic_ppocr_mobile_v2.0_rec) |
| en_ppocr_mobile_v2.0_table_rec | rec | [Download](en_ppocr_mobile_v2.0_table_rec) |
| en_ppocr_mobile_v2.0_number_rec | rec | [Download](en_ppocr_mobile_v2.0_number_rec) |
| devanagari_ppocr_mobile_v2.0_rec | rec | [Download](devanagari_ppocr_mobile_v2.0_rec) |






[ch_ppocr_mobile_v2.0_cls]:https://bj.bcebos.com/v1/ai-studio-online/0c29ed105d984b7bba9c09ecb6dcde7075330fd74fa7449fafca316603e1aaed?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_cls.onnx

[ch_ppocr_mobile_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/55d7b7e1890c4b81ae17a2d0c4b457d89f47a05407be4563a5b2e212b3fdf70b?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_det.onnx
[ch_ppocr_server_v2.0_det]:https://bj.bcebos.com/v1/ai-studio-online/65e5a792fa464c2994814b0a2af2334ada2a9c8150fa42f6ab3cfd22bb744708?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_server_v2.0_det.onnx
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