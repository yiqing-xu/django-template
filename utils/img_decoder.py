#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 09:28
# @Author  : xuyiqing
# @File    : img_decoder.py
import re
import os
import base64
import uuid
import datetime


class ImageDecoder(object):
    """
    富文本解码图片base64，保存并替换为src=url
    """

    def __init__(self, request=None):
        self.request = request
        self.image_regex = re.compile(r'<img[^>]+?/>', flags=re.S)
        self.src_regex = re.compile(r'src="data:image/(.+);base64,(.+?)"')

    def __call__(self, encode_html):
        decode_html = self.re_img_label(encode_html=encode_html)
        return decode_html

    def re_img_label(self, encode_html):
        imgs = re.sub(self.image_regex, self.re_src_label,  encode_html)
        return imgs

    def re_src_label(self, imgs):
        srcs = re.sub(self.src_regex, self.sub_src, imgs.group())
        return srcs

    def sub_src(self, data):
        img_format, img_base64 = data.group(1), data.group(2)
        missing_padding = 4 - len(img_base64) % 4
        if missing_padding:
            img_base64 += '=' * missing_padding
        image_data = base64.b64decode(img_base64)

        img_name = '{}.{}'.format(uuid.uuid4(), img_format)
        img_dir = 'media/upload/{}'.format(datetime.date.today().strftime('%Y/%m/%d'))
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        img_path = os.path.join(img_dir, img_name)

        with open(img_path, 'wb') as w:
            w.write(image_data)

        img_path = '/' + img_path
        if self.request:
            img_path = self.request.build_absolute_uri(img_path)
        return 'src="{}"'.format(img_path)


if __name__ == '__main__':
    from pydocx import PyDocX
    text = PyDocX.to_html('./test.docx')
    decoder = ImageDecoder()
    html = decoder(text)
    print(html)
