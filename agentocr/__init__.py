import cv2
import numpy as np
import onnxruntime as ort

from .infer import TextSystem, predict_system
from .infer import TextDetector, predict_det
from .infer import TextClassifier, predict_cls
from .infer import TextRecognizer, predict_rec
from .infer.utility import parse_args, init_args, get_config, get_logger, init_args

logger = get_logger()


class OCRSystem:
    def __init__(self, config='ch', warmup=True, **kwargs):
        '''
        The Inference OCR System of AgentOCR.

        Params:
            config: the name or path of the configuration file, default 'ch'.
            warmup: warm up the model during initialization, default True.
            **kwargs: more config of the OCRSystem, these options override the same options in the configuration file.
        '''
        available_providers = [
            provider[:-17] for provider in ort.get_available_providers()
        ]

        config = get_config(config)
        parser = init_args()
        self.args, self.argparse_dict = parse_args(parser, config)

        self.argparse_dict.update(kwargs)
        logger.info('OCRSystem config:{}'.format(self.argparse_dict))
        logger.info('All available providers: {}'.format(available_providers))
        self.load()

        if warmup:
            self.warmup()

    def warmup(self):
        fake_img = np.zeros((720, 1280, 3))
        for _ in range(5):
            self.text_sys.text_detector(fake_img)
            self.text_sys.text_classifier([fake_img])
            self.text_sys.text_recognizer([fake_img])

    def load(self):
        self.text_sys = TextSystem(self.args)

    def run(self, func, image_dir):
        del self.text_sys
        if self.args.total_process_num > 1:
            from multiprocessing import Process
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
        '''
        Params:
            img: the path or ndarray of the input image file.
            det: text location detection, default True.
            cls: text direction classification, default False.
            rec: text content recognition, default True.
            return_cls: return the results of text direction classification, default False.
        '''
        return self.ocr(img, det=det, cls=cls, rec=rec, return_cls=return_cls)

    def ocr(self, img, det=True, cls=False, rec=True, return_cls=False):
        '''
        Params:
            img: the path or ndarray of the input image file.
            det: text location detection, default True.
            cls: text direction classification, default False.
            rec: text content recognition, default True.
            return_cls: return the results of text direction classification, default False.
        '''
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
        from gevent.pywsgi import WSGIServer
        from .infer.server import ocr_server
        logger.info('AgentOCR server is running on http://{}:{}/'.format(
            args.host, args.port))
        server = WSGIServer((args.host, args.port), ocr_server)
        server.serve_forever()
    else:
        raise ValueError('Please check the mode.')
