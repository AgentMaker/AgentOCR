# AgentOCR Package 使用说明

## 1 快速上手

### 1.1 安装

* pip 安装：

    ```shell
    # 安装 AgentOCR
    $ pip install agentocr 

    # 根据设备平台安装合适版本的 ONNXRuntime
    $ pip install onnxruntime
    ```

* 源码安装：

    ```shell
    # 同步 AgentOCR 代码
    $ git clone https://github.com/AgentMaker/AgentOCR

    # 安装 AgentOCR 
    $ cd AgentOCR && python setup.py install

    # 根据设备平台安装合适版本的 ONNXRuntime
    $ pip install onnxruntime
    ```

## 2 使用

### 2.1 代码使用

> AgentOCR Package 会自动下载 PaddleOCR 中/英文轻量级模型作为默认模型  
可通过切换其他内置配置文件或自定义配置文件进行模型和参数自定义  
在 API 接口的使用上，基本和 PPOCR Package 保持一致

* 检测 + 方向分类器 + 识别全流程

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, cls=True)
    ```
        # 结果是一个list，每个item包含了文本框，文字和识别置信度
        [[[24.0, 36.0], [304.0, 34.0], [304.0, 72.0], [24.0, 74.0]], ['纯臻营养护发素', 0.964739]]
        [[[24.0, 80.0], [172.0, 80.0], [172.0, 104.0], [24.0, 104.0]], ['产品信息/参数', 0.98069626]]
        [[[24.0, 109.0], [333.0, 109.0], [333.0, 136.0], [24.0, 136.0]], ['（45元/每公斤，100公斤起订）', 0.9676722]]
        ......

* 检测 + 识别

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, cls=False)
    ```

        # 结果是一个list，每个item包含了文本框，文字和识别置信度
        [[[24.0, 36.0], [304.0, 34.0], [304.0, 72.0], [24.0, 74.0]], ['纯臻营养护发素', 0.964739]]
        [[[24.0, 80.0], [172.0, 80.0], [172.0, 104.0], [24.0, 104.0]], ['产品信息/参数', 0.98069626]]
        [[[24.0, 109.0], [333.0, 109.0], [333.0, 136.0], [24.0, 136.0]], ['（45元/每公斤，100公斤起订）', 0.9676722]]
        ......

* 方向分类器 + 识别

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, det=False, cls=True)
    ```

        # 结果是一个list，每个item只包含识别结果和识别置信度

        ['韩国小馆', 0.9907421]


* 单独执行检测

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, rec=False)
    ```

        # 结果是一个list，每个item只包含文本框
        [[26.0, 457.0], [137.0, 457.0], [137.0, 477.0], [26.0, 477.0]]
        [[25.0, 425.0], [372.0, 425.0], [372.0, 448.0], [25.0, 448.0]]
        [[128.0, 397.0], [273.0, 397.0], [273.0, 414.0], [128.0, 414.0]]
        ......

* 单独执行识别

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, det=False)
    ```

        # 结果是一个list，每个item只包含识别结果和识别置信度
        ['韩国小馆', 0.9907421]

* 单独执行方向分类器

    ```python
    from agentocr import OCRSystem

    # 通过 config 参数来进行模型配置，内置多国语言的配置文件
    ocr = OCRSystem(config='ch')

    # 设置测试图片路径
    img_path = 'test.jpg'

    # 调用 OCR API 进行全流程识别
    result = ocr.ocr(img_path, det=False, cls=True, rec=False)
    ```

        # 结果是一个list，每个item只包含分类结果和分类置信度
        ['0', 0.9999924]

