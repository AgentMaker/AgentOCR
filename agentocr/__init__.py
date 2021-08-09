import cv2
import numpy as np

from multiprocessing import Process

from .infer.utility import parse_args
from .infer import TextSystem, predict_system
from .infer import TextDetector, predict_det
from .infer import TextClassifier, predict_cls
from .infer import TextRecognizer, predict_rec


class OCRSystem:
    def __init__(self, config_path):
        self.args = parse_args(config_path)
        self.load()

    def load(self):
        self.text_sys = TextSystem(self.args)

    def run(self, func):
        del self.text_sys
        if self.args.total_process_num > 1:
            p_list = []
            for process_id in range(self.args.total_process_num):
                p = Process(target=func, args=(self.args, process_id))
                p.start()
                p_list.append(p)
            for p in p_list:
                p.join()
        else:
            func(self.args)
        self.load()

    def __call__(self, img, det=True, cls=True, rec=True, return_cls=False):
        return self.ocr(img, det=det, cls=cls, rec=rec, return_cls=return_cls)

    def ocr(self, img, det=True, cls=True, rec=True, return_cls=False):
        if isinstance(img, np.ndarray):
            results = self.text_sys(img, det=det, cls=cls, rec=rec, return_cls=return_cls)
        elif isinstance(img, str):
            results = self.text_sys(cv2.imread(img), det=det, cls=cls, rec=rec, return_cls=return_cls)
        return results

    def predict_det(self):
        self.run(predict_det)

    def predict_cls(self):
        self.run(predict_cls)

    def predict_rec(self):
        self.run(predict_rec)

    def predict_system(self):
        self.run(predict_system)