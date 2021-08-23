# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import cv2
import copy
import time
import logging

from PIL import Image

from .det import TextDetector
from .cls import TextClassifier
from .rec import TextRecognizer
from .utility import draw_ocr_box_txt, get_rotate_crop_image
from .utility import get_image_file_list, check_and_read_gif, get_logger, parse_args, get_vis_font, init_args

logger = get_logger()


class TextSystem(object):
    def __init__(self, args):
        if not args.show_log:
            logger.setLevel(logging.INFO)

        self.text_detector = TextDetector(args)
        self.text_classifier = TextClassifier(args)
        self.text_recognizer = TextRecognizer(args)
        self.drop_score = args.drop_score

    def print_draw_crop_rec_res(self, img_crop_list, rec_res):
        bbox_num = len(img_crop_list)
        for bno in range(bbox_num):
            cv2.imwrite("./output/img_crop_%d.jpg" % bno, img_crop_list[bno])
            logger.info(bno, rec_res[bno])

    def __call__(self, img, det=True, cls=False, rec=True, return_cls=False):
        if det:
            dt_boxes, elapse = self.text_detector(img)

            logger.debug("dt_boxes num : {}, elapse : {}".format(
                len(dt_boxes), elapse))

            if dt_boxes is None:
                return None, None

            img_crop_list = []
            dt_boxes = sorted_boxes(dt_boxes)

            for bno in range(len(dt_boxes)):
                tmp_box = copy.deepcopy(dt_boxes[bno])
                img_crop = get_rotate_crop_image(img, tmp_box)
                img_crop_list.append(img_crop)

            dt_boxes = [box.astype('float').tolist() for box in dt_boxes]
        else:
            img_crop_list = [img]

        if cls:
            img_crop_list, angle_list, elapse = self.text_classifier(
                img_crop_list)
            logger.debug("cls num  : {}, elapse : {}".format(
                len(img_crop_list), elapse))

        if rec:
            rec_res, elapse = self.text_recognizer(img_crop_list)
            logger.debug("rec_res num  : {}, elapse : {}".format(
                len(rec_res), elapse))

        results = []
        if det and rec:
            if return_cls and cls:
                for box, rec_reuslt, angle in zip(dt_boxes, rec_res,
                                                  angle_list):
                    _, score = rec_reuslt
                    if score >= self.drop_score:
                        results.append([box, rec_reuslt, angle])
            else:
                for box, rec_reuslt in zip(dt_boxes, rec_res):
                    _, score = rec_reuslt
                    if score >= self.drop_score:
                        results.append([box, rec_reuslt])
        elif rec:
            if return_cls and cls:
                for rec_reuslt, angle in zip(rec_res, angle_list):
                    _, score = rec_reuslt
                    if score >= self.drop_score:
                        results.append([rec_reuslt, angle])
            else:
                for rec_reuslt in rec_res:
                    _, score = rec_reuslt
                    if score >= self.drop_score:
                        results.append(rec_reuslt)
        elif det:
            if return_cls and cls:
                for det_reuslt, angle in zip(dt_boxes, angle_list):
                    results.append([det_reuslt, angle])
            else:
                results = dt_boxes

        elif cls:
            results = angle_list

        return results


def sorted_boxes(dt_boxes):
    """
    Sort text boxes in order from top to bottom, left to right
    args:
        dt_boxes(array):detected text boxes with shape [4, 2]
    return:
        sorted boxes(array) with shape [4, 2]
    """
    num_boxes = dt_boxes.shape[0]
    sorted_boxes = sorted(dt_boxes, key=lambda x: (x[0][1], x[0][0]))
    _boxes = list(sorted_boxes)

    for i in range(num_boxes - 1):
        if abs(_boxes[i + 1][0][1] - _boxes[i][0][1]) < 10 and \
                (_boxes[i + 1][0][0] < _boxes[i][0][0]):
            tmp = _boxes[i]
            _boxes[i] = _boxes[i + 1]
            _boxes[i + 1] = tmp
    return _boxes


def main(args, image_dir, process_id=0):
    image_file_list = get_image_file_list(image_dir)
    image_file_list = image_file_list[process_id::args.total_process_num]
    text_sys = TextSystem(args)
    is_visualize = True
    font_path = get_vis_font(args.vis_font_path)
    drop_score = args.drop_score

    total_time = 0
    _st = time.time()
    for idx, image_file in enumerate(image_file_list):

        img, flag = check_and_read_gif(image_file)
        if not flag:
            img = cv2.imread(image_file)
        if img is None:
            logger.info("error in loading image:{}".format(image_file))
            continue
        starttime = time.time()
        results = text_sys(img)

        elapse = time.time() - starttime
        total_time += elapse

        logger.info(
            str(idx) + "  Predict time of %s: %.3fs" % (image_file, elapse))
        for _, (text, score) in results:
            logger.info("{}, {:.3f}".format(text, score))

        if is_visualize:
            image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            boxes = [results[i][0] for i in range(len(results))]
            txts = [results[i][1][0] for i in range(len(results))]
            scores = [results[i][1][1] for i in range(len(results))]

            draw_img = draw_ocr_box_txt(image,
                                        boxes,
                                        txts,
                                        scores,
                                        drop_score=drop_score,
                                        font_path=font_path)
            draw_img_save = "./inference_results/"
            if not os.path.exists(draw_img_save):
                os.makedirs(draw_img_save)
            if flag:
                image_file = image_file[:-3] + "png"
            cv2.imwrite(
                os.path.join(draw_img_save, os.path.basename(image_file)),
                draw_img[:, :, ::-1])
            logger.info("The visualized image saved in {}".format(
                os.path.join(draw_img_save, os.path.basename(image_file))))

    logger.info("The predict total time is {}".format(time.time() - _st))
    logger.info("\nThe predict total time is {}".format(total_time))


if __name__ == "__main__":
    parser = init_args()
    main(parse_args(parser))
