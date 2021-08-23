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
import sys
import cv2
import wget
import json
import math
import imghdr
import logging
import argparse
import functools
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageDraw, ImageFont

file_path = os.path.abspath(__file__)
infer_dir = os.path.dirname(file_path)
package_dir = os.path.dirname(infer_dir)

model_urls = {
    'cls': {
        'ch_ppocr_mobile_v2.0_cls':
        'https://bj.bcebos.com/v1/ai-studio-online/0c29ed105d984b7bba9c09ecb6dcde7075330fd74fa7449fafca316603e1aaed?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_cls.onnx',
    },
    'det': {
        'ch_ppocr_mobile_v2.0_det':
        'https://bj.bcebos.com/v1/ai-studio-online/55d7b7e1890c4b81ae17a2d0c4b457d89f47a05407be4563a5b2e212b3fdf70b?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_det.onnx',
        'ch_ppocr_server_v2.0_det':
        'https://bj.bcebos.com/v1/ai-studio-online/65e5a792fa464c2994814b0a2af2334ada2a9c8150fa42f6ab3cfd22bb744708?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_server_v2.0_det.onnx',
        'en_ppocr_mobile_v2.0_det':
        'https://bj.bcebos.com/v1/ai-studio-online/e02ba8dfb2b34febb9c468114031ca7f4a6e320359a14f5aaa4067b66c3d99bf?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_det.onnx',
        'en_ppocr_mobile_v2.0_table_det':
        'https://bj.bcebos.com/v1/ai-studio-online/d28ba772eb1d48a582a7ce16894885d662399f1ee12a4bfaa73d2b4987c3dc31?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_table_det.onnx',
    },
    'rec': {
        'ch_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/77e67a9bb1cc421a97e037462838f159526b2d0ba3d94a3eb0da35408174edb7?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_mobile_v2.0_rec.onnx',
        'ch_ppocr_server_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/5f6546d18a84448486abe778b9f1b1ba21da2efbd6b84aaa808936e94771ec68?responseContentDisposition=attachment%3B%20filename%3Dch_ppocr_server_v2.0_rec.onnx',
        'ka_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/85cdc2462b6f4ff3a3474b724a33308112b3c55d9bf541469b858b0b0035872c?responseContentDisposition=attachment%3B%20filename%3Dka_mobile_v2.0_rec.onnx',
        'te_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/a6d61a705348461b93821b963769ddb56502e57bdc47470d9e8c7ed29f80c016?responseContentDisposition=attachment%3B%20filename%3Dte_mobile_v2.0_rec.onnx',
        'ta_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/ef955098816b47be82538a9fff2487516a8a5da3ec454b689406e01b4031fd41?responseContentDisposition=attachment%3B%20filename%3Dta_mobile_v2.0_rec.onnx',
        'cht_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/85d2cfd9c24e47319ebb48184f4e8ed3cdef007a8731476eb8efbd3d7b4f5ff9?responseContentDisposition=attachment%3B%20filename%3Dchinese_cht_mobile_v2.0_rec.onnx',
        'japan_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/df453e13ad144138978ac3d121b5ec73adfccd9a014e4d1281fe9a4015e2cf92?responseContentDisposition=attachment%3B%20filename%3Djapan_mobile_v2.0_rec.onnx',
        'latin_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/159e47bf6fab45efbe786dc4d932cd71d28f74b0bf9e4144b82f00ebd1a467a5?responseContentDisposition=attachment%3B%20filename%3Dlatin_ppocr_mobile_v2.0_rec.onnx',
        'arabic_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/27521b051c96454eb10f13f403ca699a819d997e6d2d4afa9721f2f80ad3aed7?responseContentDisposition=attachment%3B%20filename%3Darabic_ppocr_mobile_v2.0_rec.onnx',
        'korean_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/20d94b1440654ed9aadbe61b565430702629de85021a4e14ad644fae5896ed77?responseContentDisposition=attachment%3B%20filename%3Dkorean_mobile_v2.0_rec.onnx',
        'french_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/cdc0503a71274172b0d43e07a7c285745231381b52d34be584babe1e1202a9d9?responseContentDisposition=attachment%3B%20filename%3Dfrench_mobile_v2.0_rec.onnx',
        'german_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/87356bfc558f481fbeaae6fa28b6ea50194c2ae94f4d4165a95927dd9ad4d669?responseContentDisposition=attachment%3B%20filename%3Dgerman_mobile_v2.0_rec.onnx',
        'cyrillic_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/3f3b53e4b2b74cedaa24b4998e35d4b1c527cc7eb3f645859695de80bb14b625?responseContentDisposition=attachment%3B%20filename%3Dcyrillic_ppocr_mobile_v2.0_rec.onnx',
        'en_ppocr_mobile_v2.0_table_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/c9d6e42c99fe40ae9448ee9d07973d2b603f1e68fffa4a29b8f8cc45b3dc16f5?responseContentDisposition=attachment%3B%20filename%3Den_ppocr_mobile_v2.0_table_rec.onnx',
        'en_ppocr_mobile_v2.0_number_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/a31fc2aed28841b4ac861c7ae4639d3f62b102d7f5e0416088544a9763affeec?responseContentDisposition=attachment%3B%20filename%3Den_number_mobile_v2.0_rec.onnx',
        'devanagari_ppocr_mobile_v2.0_rec':
        'https://bj.bcebos.com/v1/ai-studio-online/a78a9384579d451988858aa97e99d4cc2518902128174b089fabac2a150c8822?responseContentDisposition=attachment%3B%20filename%3Ddevanagari_ppocr_mobile_v2.0_rec.onnx',
    }
}


def get_config(config):
    if os.path.isfile(config):
        return config
    else:
        latin_language = [
            'af', 'az', 'bs', 'cs', 'cy', 'da', 'de', 'es', 'et', 'fr', 'ga',
            'hr', 'hu', 'id', 'is', 'it', 'ku', 'la', 'lt', 'lv', 'mi', 'ms',
            'mt', 'nl', 'no', 'oc', 'pi', 'pl', 'pt', 'ro', 'rs_latin', 'sk',
            'sl', 'sq', 'sv', 'sw', 'tl', 'tr', 'uz', 'vi'
        ]
        arabic_language = ['ar', 'fa', 'ug', 'ur']
        cyrillic_language = [
            'ru', 'rs_cyrillic', 'be', 'bg', 'uk', 'mn', 'abq', 'ady', 'kbd',
            'ava', 'dar', 'inh', 'che', 'lbe', 'lez', 'tab'
        ]
        devanagari_language = [
            'hi', 'mr', 'ne', 'bh', 'mai', 'ang', 'bho', 'mah', 'sck', 'new',
            'gom', 'sa', 'bgc'
        ]
        others_language = [
            'ch', 'cht', 'en', 'french', 'german', 'japan', 'ka', 'ta', 'te',
            'korean'
        ]

        if config in latin_language:
            language = "latin"
        elif config in arabic_language:
            language = "arabic"
        elif config in cyrillic_language:
            language = "cyrillic"
        elif config in devanagari_language:
            language = "devanagari"
        elif config in others_language:
            language = config
        else:
            raise ValueError('Please check your config.')

        config = os.path.join(package_dir, 'resources', 'configs',
                              language + '.json')
        return config


def get_char_dict(char_dict_path):
    if not os.path.isfile(char_dict_path):
        temp_path = os.path.join(package_dir, 'resources', 'char_dicts',
                                 char_dict_path)
        if os.path.isfile(temp_path):
            char_dict_path = temp_path
        elif os.path.isfile(temp_path + '.txt'):
            char_dict_path = temp_path + '.txt'
    return char_dict_path


def get_vis_font(vis_font_path):
    if not os.path.isfile(vis_font_path):
        temp_path = os.path.join(package_dir, 'resources', 'fonts',
                                 vis_font_path)
        if os.path.isfile(temp_path):
            vis_font_path = temp_path
        elif os.path.isfile(temp_path + '.ttf'):
            vis_font_path = temp_path + '.ttf'
    return vis_font_path


def str2providers(str, logger):
    available_providers = ort.get_available_providers()

    if str.lower() == 'auto':
        return available_providers

    providers_dict = {
        provider.lower(): provider
        for provider in available_providers
    }

    provider_strs = [(provider_str + 'ExecutionProvider').lower()
                     for provider_str in str.split(',')]

    select_providers = [
        providers_dict[provider_str] for provider_str in provider_strs
        if provider_str in providers_dict.keys()
    ]

    if len(select_providers) == 0:
        logger.error('No available providers: {}'.format(str.split(',')))
        logger.error(
            'Automatically sets the available providers as the default providers!'
            .format(str.split(',')))
        select_providers = available_providers

    return select_providers


def init_args():
    parser = argparse.ArgumentParser()

    # params for onnx engine
    parser.add_argument("--providers", type=str, default='auto')

    # params for text detector
    parser.add_argument("--det_algorithm", type=str, default='DB')
    parser.add_argument("--det_model_dir", type=str, default='ch_ppocr_mobile_v2.0_det')
    parser.add_argument("--det_limit_side_len", type=float, default=960)
    parser.add_argument("--det_limit_type", type=str, default='max')

    # DB parmas
    parser.add_argument("--det_db_thresh", type=float, default=0.3)
    parser.add_argument("--det_db_box_thresh", type=float, default=0.6)
    parser.add_argument("--det_db_unclip_ratio", type=float, default=1.5)
    parser.add_argument("--use_dilation", type=bool, default=False)
    parser.add_argument("--det_db_score_mode", type=str, default="fast")

    # EAST parmas
    parser.add_argument("--det_east_score_thresh", type=float, default=0.8)
    parser.add_argument("--det_east_cover_thresh", type=float, default=0.1)
    parser.add_argument("--det_east_nms_thresh", type=float, default=0.2)

    # SAST parmas
    parser.add_argument("--det_sast_score_thresh", type=float, default=0.5)
    parser.add_argument("--det_sast_nms_thresh", type=float, default=0.2)
    parser.add_argument("--det_sast_polygon", type=bool, default=False)

    # params for text recognizer
    parser.add_argument("--rec_algorithm", type=str, default='CRNN')
    parser.add_argument("--rec_model_dir", type=str, default='ch_ppocr_mobile_v2.0_rec')
    parser.add_argument("--rec_image_shape", type=str, default="3, 32, 320")
    parser.add_argument("--rec_char_type", type=str, default='ch')
    parser.add_argument("--rec_batch_num", type=int, default=8)
    parser.add_argument("--max_text_length", type=int, default=25)
    parser.add_argument("--rec_char_dict_path", type=str, default="ppocr_keys_v1")
    parser.add_argument("--use_space_char", type=bool, default=True)
    parser.add_argument("--vis_font_path", type=str, default="simfang")
    parser.add_argument("--drop_score", type=float, default=0.5)

    # params for text classifier
    parser.add_argument("--cls_model_dir", type=str, default='ch_ppocr_mobile_v2.0_cls')
    parser.add_argument("--cls_image_shape", type=str, default="3, 48, 192")
    parser.add_argument("--label_list", type=list, default=['0', '180'])
    parser.add_argument("--cls_batch_num", type=int, default=8)
    parser.add_argument("--cls_thresh", type=float, default=0.9)

    # multi-process
    parser.add_argument("--total_process_num", type=int, default=1)

    # params for config
    parser.add_argument("--show_log", type=bool, default=True)

    return parser


def parse_args(parser, config=None):
    args = parser.parse_known_args()[0]
    argparse_dict = vars(args)

    if config:
        with open(config, 'r', encoding='UTF-8') as f:
            json_dict = json.load(f)
        argparse_dict.update(json_dict)

    return args, argparse_dict


def create_session(args, mode, logger):
    if mode == "det":
        model_dir = args.det_model_dir
    elif mode == 'cls':
        model_dir = args.cls_model_dir
    elif mode == 'rec':
        model_dir = args.rec_model_dir
    elif mode == 'table':
        model_dir = args.table_model_dir
    else:
        model_dir = args.e2e_model_dir

    if model_dir in model_urls[mode]:
        url = model_urls[mode][model_dir]
        if not os.path.exists('pretrained_models'):
            os.mkdir('pretrained_models')
        model_dir = os.path.join('pretrained_models', model_dir + '.onnx')
        if not os.path.isfile(model_dir):
            wget.download(url, out=model_dir)

    if model_dir is None:
        logger.info("not find {} model file path {}".format(mode, model_dir))
        sys.exit(0)

    sess_options = ort.SessionOptions()
    providers = str2providers(args.providers, logger)
    logger.info('Using providers: {}'.format(
        [provider[:-17] for provider in providers]))

    if 'DmlExecutionProvider' in providers:
        logger.info('Disable mem_pattern because using the Dml Provider.')
        sess_options.enable_mem_pattern = False

    session = ort.InferenceSession(model_dir,
                                   providers=providers,
                                   sess_options=sess_options)

    input_names = [input.name for input in session.get_inputs()]

    output_names = [output.name for output in session.get_outputs()]

    return session, input_names, output_names


def draw_text_det_res(dt_boxes, img_path):
    src_im = cv2.imread(img_path)
    for box in dt_boxes:
        box = np.array(box).astype(np.int32).reshape(-1, 2)
        cv2.polylines(src_im, [box], True, color=(255, 255, 0), thickness=2)
    return src_im


def resize_img(img, input_size=600):
    """
    resize img and limit the longest side of the image to input_size
    """
    img = np.array(img)
    im_shape = img.shape
    im_size_max = np.max(im_shape[0:2])
    im_scale = float(input_size) / float(im_size_max)
    img = cv2.resize(img, None, None, fx=im_scale, fy=im_scale)
    return img


def draw_ocr(image,
             boxes,
             txts=None,
             scores=None,
             drop_score=0.5,
             font_path="./doc/fonts/simfang.ttf"):
    """
    Visualize the results of OCR detection and recognition
    args:
        image(Image|array): RGB image
        boxes(list): boxes with shape(N, 4, 2)
        txts(list): the texts
        scores(list): txxs corresponding scores
        drop_score(float): only scores greater than drop_threshold will be visualized
        font_path: the path of font which is used to draw text
    return(array):
        the visualized img
    """
    if scores is None:
        scores = [1] * len(boxes)

    box_num = len(boxes)

    for i in range(box_num):
        if scores is not None and (scores[i] < drop_score
                                   or math.isnan(scores[i])):
            continue
        box = np.reshape(np.array(boxes[i]), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)

    if txts is not None:
        img = np.array(resize_img(image, input_size=600))
        txt_img = text_visual(txts,
                              scores,
                              img_h=img.shape[0],
                              img_w=600,
                              threshold=drop_score,
                              font_path=font_path)
        img = np.concatenate([np.array(img), np.array(txt_img)], axis=1)
        return img
    return image


def draw_ocr_box_txt(image,
                     boxes,
                     txts,
                     scores=None,
                     drop_score=0.5,
                     font_path="./doc/simfang.ttf"):
    h, w = image.height, image.width
    img_left = image.copy()
    img_right = Image.new('RGB', (w, h), (255, 255, 255))

    import random

    random.seed(0)
    draw_left = ImageDraw.Draw(img_left)
    draw_right = ImageDraw.Draw(img_right)

    for idx, (box, txt) in enumerate(zip(boxes, txts)):
        if scores is not None and scores[idx] < drop_score:
            continue
        color = (random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255))
        draw_left.polygon([tuple(point) for point in box], fill=color)
        draw_right.polygon([
            box[0][0], box[0][1], box[1][0], box[1][1], box[2][0], box[2][1],
            box[3][0], box[3][1]
        ],
                           outline=color)
        box_height = math.sqrt((box[0][0] - box[3][0])**2 +
                               (box[0][1] - box[3][1])**2)
        box_width = math.sqrt((box[0][0] - box[1][0])**2 +
                              (box[0][1] - box[1][1])**2)

        if box_height > 2 * box_width:
            font_size = max(int(box_width * 0.9), 10)
            font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
            cur_y = box[0][1]
            for c in txt:
                char_size = font.getsize(c)
                draw_right.text((box[0][0] + 3, cur_y),
                                c,
                                fill=(0, 0, 0),
                                font=font)
                cur_y += char_size[1]
        else:
            font_size = max(int(box_height * 0.8), 10)
            font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
            draw_right.text([box[0][0], box[0][1]],
                            txt,
                            fill=(0, 0, 0),
                            font=font)

    img_left = Image.blend(image, img_left, 0.5)
    img_show = Image.new('RGB', (w * 2, h), (255, 255, 255))
    img_show.paste(img_left, (0, 0, w, h))
    img_show.paste(img_right, (w, 0, w * 2, h))
    return np.array(img_show)


def str_count(s):
    """
    Count the number of Chinese characters,
    a single English character and a single number
    equal to half the length of Chinese characters.
    args:
        s(string): the input of string
    return(int):
        the number of Chinese characters
    """
    import string
    count_zh = count_pu = 0
    s_len = len(s)
    en_dg_count = 0
    for c in s:
        if c in string.ascii_letters or c.isdigit() or c.isspace():
            en_dg_count += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    return s_len - math.ceil(en_dg_count / 2)


def text_visual(texts,
                scores,
                img_h=400,
                img_w=600,
                threshold=0.,
                font_path="./doc/simfang.ttf"):
    """
    create new blank img and draw txt on it
    args:
        texts(list): the text will be draw
        scores(list|None): corresponding score of each txt
        img_h(int): the height of blank img
        img_w(int): the width of blank img
        font_path: the path of font which is used to draw text
    return(array):
    """
    if scores is not None:
        assert len(texts) == len(
            scores), "The number of txts and corresponding scores must match"

    def create_blank_img():
        blank_img = np.ones(shape=[img_h, img_w], dtype=np.int8) * 255
        blank_img[:, img_w - 1:] = 0
        blank_img = Image.fromarray(blank_img).convert("RGB")
        draw_txt = ImageDraw.Draw(blank_img)
        return blank_img, draw_txt

    blank_img, draw_txt = create_blank_img()

    font_size = 20
    txt_color = (0, 0, 0)
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")

    gap = font_size + 5
    txt_img_list = []
    count, index = 1, 0
    for idx, txt in enumerate(texts):
        index += 1
        if scores[idx] < threshold or math.isnan(scores[idx]):
            index -= 1
            continue
        first_line = True
        while str_count(txt) >= img_w // font_size - 4:
            tmp = txt
            txt = tmp[:img_w // font_size - 4]
            if first_line:
                new_txt = str(index) + ': ' + txt
                first_line = False
            else:
                new_txt = '    ' + txt
            draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
            txt = tmp[img_w // font_size - 4:]
            if count >= img_h // gap - 1:
                txt_img_list.append(np.array(blank_img))
                blank_img, draw_txt = create_blank_img()
                count = 0
            count += 1
        if first_line:
            new_txt = str(index) + ': ' + txt + '   ' + '%.3f' % (scores[idx])
        else:
            new_txt = "  " + txt + "  " + '%.3f' % (scores[idx])
        draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
        # whether add new blank img or not
        if count >= img_h // gap - 1 and idx + 1 < len(texts):
            txt_img_list.append(np.array(blank_img))
            blank_img, draw_txt = create_blank_img()
            count = 0
        count += 1
    txt_img_list.append(np.array(blank_img))
    if len(txt_img_list) == 1:
        blank_img = np.array(txt_img_list[0])
    else:
        blank_img = np.concatenate(txt_img_list, axis=1)
    return np.array(blank_img)


def base64_to_cv2(b64str):
    import base64
    data = base64.b64decode(b64str.encode('utf8'))
    data = np.fromstring(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data


def draw_boxes(image, boxes, scores=None, drop_score=0.5):
    if scores is None:
        scores = [1] * len(boxes)
    for (box, score) in zip(boxes, scores):
        if score < drop_score:
            continue
        box = np.reshape(np.array(box), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
    return image


def get_rotate_crop_image(img, points):
    '''
    img_height, img_width = img.shape[0:2]
    left = int(np.min(points[:, 0]))
    right = int(np.max(points[:, 0]))
    top = int(np.min(points[:, 1]))
    bottom = int(np.max(points[:, 1]))
    img_crop = img[top:bottom, left:right, :].copy()
    points[:, 0] = points[:, 0] - left
    points[:, 1] = points[:, 1] - top
    '''
    assert len(points) == 4, "shape of points must be 4*2"
    img_crop_width = int(
        max(np.linalg.norm(points[0] - points[1]),
            np.linalg.norm(points[2] - points[3])))
    img_crop_height = int(
        max(np.linalg.norm(points[0] - points[3]),
            np.linalg.norm(points[1] - points[2])))
    pts_std = np.float32([[0, 0], [img_crop_width, 0],
                          [img_crop_width, img_crop_height],
                          [0, img_crop_height]])
    M = cv2.getPerspectiveTransform(points, pts_std)
    dst_img = cv2.warpPerspective(img,
                                  M, (img_crop_width, img_crop_height),
                                  borderMode=cv2.BORDER_REPLICATE,
                                  flags=cv2.INTER_CUBIC)
    dst_img_height, dst_img_width = dst_img.shape[0:2]
    if dst_img_height * 1.0 / dst_img_width >= 1.5:
        dst_img = np.rot90(dst_img)
    return dst_img


###################################################################


def print_dict(d, logger, delimiter=0):
    """
    Recursively visualize a dict and
    indenting acrrording by the relationship of keys.
    """
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            logger.info("{}{} : ".format(delimiter * " ", str(k)))
            print_dict(v, logger, delimiter + 4)
        elif isinstance(v, list) and len(v) >= 1 and isinstance(v[0], dict):
            logger.info("{}{} : ".format(delimiter * " ", str(k)))
            for value in v:
                print_dict(value, logger, delimiter + 4)
        else:
            logger.info("{}{} : {}".format(delimiter * " ", k, v))


def get_check_global_params(mode):
    check_params = ['use_gpu', 'max_text_length', 'image_shape', \
                    'image_shape', 'character_type', 'loss_type']
    if mode == "train_eval":
        check_params = check_params + [ \
            'train_batch_size_per_card', 'test_batch_size_per_card']
    elif mode == "test":
        check_params = check_params + ['test_batch_size_per_card']
    return check_params


def get_image_file_list(img_file):
    imgs_lists = []
    if img_file is None or not os.path.exists(img_file):
        raise Exception("not found any img file in {}".format(img_file))

    img_end = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif', 'tiff', 'gif', 'GIF'}
    if os.path.isfile(img_file) and imghdr.what(img_file) in img_end:
        imgs_lists.append(img_file)
    elif os.path.isdir(img_file):
        for single_file in os.listdir(img_file):
            file_path = os.path.join(img_file, single_file)
            if os.path.isfile(file_path) and imghdr.what(file_path) in img_end:
                imgs_lists.append(file_path)
    if len(imgs_lists) == 0:
        raise Exception("not found any img file in {}".format(img_file))
    imgs_lists = sorted(imgs_lists)
    return imgs_lists


def check_and_read_gif(img_path):
    if os.path.basename(img_path)[-3:] in ['gif', 'GIF']:
        gif = cv2.VideoCapture(img_path)
        ret, frame = gif.read()
        if not ret:
            logger = logging.getLogger('ppocr')
            logger.info("Cannot read {}. This gif image maybe corrupted.")
            return None, False
        if len(frame.shape) == 2 or frame.shape[-1] == 1:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        imgvalue = frame[:, :, ::-1]
        return imgvalue, True
    return None, False


logger_initialized = {}


@functools.lru_cache()
def get_logger(name='root', log_file=None, log_level=logging.DEBUG):
    """Initialize and get a logger by name.
    If the logger has not been initialized, this method will initialize the
    logger by adding one or two handlers, otherwise the initialized logger will
    be directly returned. During initialization, a StreamHandler will always be
    added. If `log_file` is specified a FileHandler will also be added.
    Args:
        name (str): Logger name.
        log_file (str | None): The log filename. If specified, a FileHandler
            will be added to the logger.
        log_level (int): The logger level. Note that only the process of
            rank 0 is affected, and other processes will set the level to
            "Error" thus be silent most of the time.
    Returns:
        logging.Logger: The expected logger.
    """
    logger = logging.getLogger(name)
    if name in logger_initialized:
        return logger
    for logger_name in logger_initialized:
        if name.startswith(logger_name):
            return logger

    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt="%Y/%m/%d %H:%M:%S")

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(log_level)
    logger_initialized[name] = True
    return logger


if __name__ == '__main__':
    pass
