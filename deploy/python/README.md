# Python 推理部署
## 特性
* 项目基于 PaddleOCR 开发，但与 PaddleOCR 完成解耦，无需依赖 PaddleOCR 项目即可直接运行
* 兼容 ONNX 和 Paddle 两种后端，可通过参数进行直接切换
* 支持 ONNXRuntime 的 CPU CUDA DirectML 等 Providers

## 依赖环境
* 必须依赖项：

    ```shell
    cycler==0.10.0
    flatbuffers==2.0
    imageio==2.9.0
    kiwisolver==1.3.1
    matplotlib==3.4.2
    networkx==2.6.1
    numpy==1.21.1
    opencv-python==4.5.3.56
    pandas==1.3.0
    Pillow==8.3.1
    protobuf==3.17.3
    pyclipper==1.3.0
    pyparsing==2.4.7
    python-dateutil==2.8.2
    pytz==2021.1
    PyWavelets==1.1.1
    scikit-image==0.18.2
    scipy==1.7.0
    Shapely==1.7.1
    six==1.16.0
    tifffile==2021.7.2
    ```
* 可选依赖项：

    ```shell
    onnxruntime
    paddlepaddle
    ```