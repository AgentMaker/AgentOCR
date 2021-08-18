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

* whl 包安装：

    * 下载 whl 包：[链接](https://github.com/AgentMaker/AgentOCR/releases)

    * 安装 whl 包：

        ```shell
        # 安装 AgentOCR
        $ pip install agentocr-x.x.x-py3-none-any.whl 
        
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

> AgentOCR Package 会自动下载 PaddleOCR 中/英文轻量级模型作为默认模型  
可通过切换其他内置配置文件或自定义配置文件进行模型和参数自定义  
在 API 接口的使用上，基本和 PPOCR Package 保持一致

### 2.1 代码使用

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

## 3 配置

> AgentOCR 使用 json 格式的配置文件来配置各种模型和各项参数  
也同时内置了多个语言的预设参数配置，可通过对应的语言缩写进行快速调用  
具体的语言和缩写的对应情况，请参考主页的 [【多语言支持】](../README.md#多语言支持) 表格  
更多 PPOCR 的预训练模型，请跳转至主页 [【预训练模型】](../README.md#预训练模型) 处下载  

### 3.1 配置文件
* 快速配置：

    > 可通过如下几个选项快速配置不同的模型文件、字典和可视化字体

    ```json
    {
        "det_model_dir": "ch_ppocr_mobile_v2.0_det",
        "rec_model_dir": "ch_ppocr_mobile_v2.0_rec",
        "rec_char_type": "ch",
        "rec_char_dict_path": "ppocr_keys_v1",
        "vis_font_path": "simfang",
        "cls_model_dir": "ch_ppocr_mobile_v2.0_cls"
    }
    ```

* 完整配置：

    > 详细的参数介绍请参考下一小节的内容

    ```json
    {
        "providers": "CPU",
        "det_algorithm": "DB",
        "det_model_dir": "ch_ppocr_mobile_v2.0_det",
        "det_limit_side_len": 960,
        "det_limit_type": "max",
        "det_db_thresh": 0.3,
        "det_db_box_thresh": 0.6,
        "det_db_unclip_ratio": 1.5,
        "max_batch_size": 10,
        "use_dilation": false,
        "det_db_score_mode": "fast",
        "det_east_score_thresh": 0.8,
        "det_east_cover_thresh": 0.1,
        "det_east_nms_thresh": 0.2,
        "det_sast_score_thresh": 0.5,
        "det_sast_nms_thresh": 0.2,
        "det_sast_polygon": false,
        "rec_algorithm": "CRNN",
        "rec_model_dir": "ch_ppocr_mobile_v2.0_rec",
        "rec_image_shape": "3, 32, 320",
        "rec_char_type": "ch",
        "rec_batch_num": 6,
        "max_text_length": 25,
        "rec_char_dict_path": "ppocr_keys_v1",
        "use_space_char": true,
        "vis_font_path": "simfang",
        "drop_score": 0.5,
        "use_angle_cls": true,
        "cls_model_dir": "ch_ppocr_mobile_v2.0_cls",
        "cls_image_shape": "3, 48, 192",
        "label_list": ["0", "180"],
        "cls_batch_num": 6,
        "cls_thresh": 0.9,
        "total_process_num": 1,
        "show_log": true
    }
    ```

### 3.2 参数说明
| 字段                    | 说明                                                                                                                                                                                                                 | 默认值                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| det_algorithm           | 使用的检测算法类型                                                                                                                                                                                                   | DB                      |
| det_model_dir          |  检测模型文件 |   None        |
| det_max_side_len        | 检测算法前向时图片长边的最大尺寸，当长边超出这个值时会将长边resize到这个大小，短边等比例缩放                                                                                                                         | 960                     |
| det_db_thresh           | DB模型输出预测图的二值化阈值                                                                                                                                                                                         | 0.3                     |
| det_db_box_thresh       | DB模型输出框的阈值，低于此值的预测框会被丢弃                                                                                                                                                                           | 0.5                     |
| det_db_unclip_ratio     | DB模型输出框扩大的比例                                                                                                                                                                                               | 2                       |
| det_east_score_thresh   | EAST模型输出预测图的二值化阈值                                                                                                                                                                                       | 0.8                     |
| det_east_cover_thresh   | EAST模型输出框的阈值，低于此值的预测框会被丢弃                                                                                                                                                                         | 0.1                     |
| det_east_nms_thresh     | EAST模型输出框NMS的阈值                                                                                                                                                                                              | 0.2                     |
| rec_algorithm           | 使用的识别算法类型                                                                                                                                                                                                   | CRNN                    |
| rec_model_dir          | 识别模型文件 | None |
| rec_image_shape         | 识别算法的输入图片尺寸                                                                                                                                                                                             | "3,32,320"              |
| rec_char_type           | 识别算法的字符类型，中英文(ch)、英文(en)、法语(french)、德语(german)、韩语(korean)、日语(japan)                                                                                                                                                                               | ch                      |
| rec_batch_num           | 进行识别时，同时前向的图片数                                                                                                                                                                                         | 30                      |
| max_text_length         | 识别算法能识别的最大文字长度                                                                                                                                                                                         | 25                      |
| rec_char_dict_path      | 识别模型字典路径，当rec_model_dir使用方式2传参时需要修改为自己的字典路径                                                                                                                                                | ./ppocr/utils/ppocr_keys_v1.txt                        |
| use_space_char          | 是否识别空格                                                                                                                                                                                                         | TRUE                    |
| drop_score          | 对输出按照分数(来自于识别模型)进行过滤，低于此分数的不返回                                                                                                                                                                                                         | 0.5                    |
| use_angle_cls          | 是否加载分类模型                                                                                                                                                                                                         | FALSE                    |
| cls_model_dir          | 分类模型文件 | None                    |
| cls_image_shape          | 分类算法的输入图片尺寸                                                                           | "3, 48, 192"                    |
| label_list          | 分类算法的标签列表                                                                           | ['0', '180']                  |
| cls_batch_num          | 进行分类时，同时前向的图片数                                                                          |30                 |
| show_log                     | 是否打印det和rec等信息                                                                                                                                                                                                | FALSE                    |