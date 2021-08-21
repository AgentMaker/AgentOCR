import cv2
import numpy as np
import onnxruntime as ort

from multiprocessing import Process

from .infer import TextSystem, predict_system
from .infer import TextDetector, predict_det
from .infer import TextClassifier, predict_cls
from .infer import TextRecognizer, predict_rec
from .infer.utility import parse_args, init_args, get_config, get_logger, init_args


class OCRSystem:
    def __init__(self, config='ch', **kwargs):
        self.logger = get_logger()
        available_providers = [
            provider[:-17] for provider in ort.get_available_providers()
        ]
        self.logger.info(
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


def command():
    parser = init_args()
    parser.add_argument(dest='mode', type=str)
    parser.add_argument(dest="image_dir", type=str)
    parser.add_argument("--config", "-c", type=str, default='ch')
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
    else:
        raise ValueError('Please check the mode.')
