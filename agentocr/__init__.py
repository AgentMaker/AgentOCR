import cv2
import json
import base64
import numpy as np
import onnxruntime as ort

from multiprocessing import Process
from flask import Flask, request
from gevent.pywsgi import WSGIServer

from .infer import TextSystem, predict_system
from .infer import TextDetector, predict_det
from .infer import TextClassifier, predict_cls
from .infer import TextRecognizer, predict_rec
from .infer.utility import parse_args, init_args, get_config, get_logger, init_args, base64_to_cv2

app = Flask(__name__)
logger = get_logger()

class OCRSystem:
    def __init__(self, config='ch', **kwargs):
        
        available_providers = [
            provider[:-17] for provider in ort.get_available_providers()
        ]
        logger.info(
            'All available providers: {}'.format(available_providers))

        config = get_config(config)
        parser = init_args()
        self.args, self.argparse_dict = parse_args(parser, config)

        self.argparse_dict.update(kwargs)
        self.load()

    def load(self):
        self.text_sys = TextSystem(self.args)

    def run(self, func, image_dir):
        del self.text_sys
        if self.args.total_process_num > 1:
            p_list = []
            for process_id in range(self.args.total_process_num):
                p = Process(target=func,
                            args=(self.args, image_dir, process_id))
                p.start()
                p_list.append(p)
            for p in p_list:
                p.join()
        else:
            func(self.args, image_dir)
        self.load()

    def __call__(self, img, det=True, cls=False, rec=True, return_cls=False):
        return self.ocr(img, det=det, cls=cls, rec=rec, return_cls=return_cls)

    def ocr(self, img, det=True, cls=False, rec=True, return_cls=False):
        if isinstance(img, np.ndarray):
            results = self.text_sys(img,
                                    det=det,
                                    cls=cls,
                                    rec=rec,
                                    return_cls=return_cls)
        elif isinstance(img, str):
            results = self.text_sys(cv2.imdecode(
                np.fromfile(img, dtype=np.uint8), 1),
                                    det=det,
                                    cls=cls,
                                    rec=rec,
                                    return_cls=return_cls)
        return results

    def predict_det(self, image_dir):
        self.run(predict_det, image_dir)

    def predict_cls(self, image_dir):
        self.run(predict_cls, image_dir)

    def predict_rec(self, image_dir):
        self.run(predict_rec, image_dir)

    def predict_system(self, image_dir):
        self.run(predict_system, image_dir)


@app.route("/ocr", methods=['POST'])
def predict_server():
    if not request.data:
        return ('fail')

    request_data = request.data.decode('utf-8')
    request_json = json.loads(request_data)

    if 'image' not in request_json:
        return ('fail')

    image_base64 = request_json.pop('image')
    image = base64_to_cv2(image_base64)
    results = ocr(image, **request_json)

    return json.dumps(results, ensure_ascii=False)


def command():
    global ocr
    parser = init_args()
    # Command mode
    parser.add_argument(dest="mode", type=str)

    # Infer image dir or path
    parser.add_argument("--image_dir", type=str)

    # OCRSystem config
    parser.add_argument("--config", type=str, default='ch')

    # Server config
    parser.add_argument("--host", type=str, default='127.0.0.1')
    parser.add_argument("--port", type=int, default=5000)

    args = parser.parse_known_args()[0]
    config = get_config(args.config)
    args, argparse_dict = parse_args(parser, config)
    ocr = OCRSystem(**argparse_dict)

    if args.mode == 'cls':
        ocr.predict_cls(args.image_dir)
    elif args.mode == 'det':
        ocr.predict_det(args.image_dir)
    elif args.mode == 'rec':
        ocr.predict_rec(args.image_dir)
    elif args.mode == 'system':
        ocr.predict_system(args.image_dir)
    elif args.mode == 'server':
        server = WSGIServer((args.host, args.port), app)
        server.serve_forever()
    else:
        raise ValueError('Please check the mode.')
