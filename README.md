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

* 本项目目前包含如下子项目：
    
    * Python Package **【AgentOCR】** 
    * OCR 标注软件 [**【AgentOCRLabeling】**](https://github.com/AgentMaker/AgentOCRLabeling)
    * 中国车牌检测识别系统 [**【AgentCLPR】**](https://github.com/AgentMaker/AgentCLPR)

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


## 使用指南
* Python Package：

    * 快速安装：

        ```shell
        # 安装 AgentOCR
        $ pip install agentocr 
        
        # 根据设备平台安装合适版本的 ONNXRuntime

        # CPU 版本（推荐非 win10 系统，无 CUDA 支持的设备安装）
        $ pip install onnxruntime

        # GPU 版本（推荐有 CUDA 支持的设备安装）
        $ pip install onnxruntime-gpu

        # DirectML 版本（推荐 win10 系统的设备安装，可实现通用的显卡加速）
        $ pip install onnxruntime-directml

        # 更多版本的安装详情请参考 ONNXRuntime 官网
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

    | 语言 | 缩写 |
    |:-:|:-:|
    |简体中文|ch|
    |繁体中文|cht|
    |英文|en|
    |法文|fr|
    |德文|ger|
    |韩文|kr|
    |日文|jp|
    |卡纳达文|ka|
    |泰卢固文|te|
    |泰米尔文|ta|
    |拉丁文|la|
    |西里尔文|cy|
    |梵文|de|

## 更多功能
* 更多功能正在持续开发中，敬请期待：

    - [x] PaddleOCR 识别模型字典优化

    - [x] PaddleOCR v2 模型支持

    - [ ] PaddleOCR Structure 模型支持

    - [ ] GUI 图形界面  

    - [ ] 中国车牌检测识别系统  

    - [ ] PaddleOCR -> ONNX 模型转换部署工具

    - [ ] 多平台的可执行标注软件  