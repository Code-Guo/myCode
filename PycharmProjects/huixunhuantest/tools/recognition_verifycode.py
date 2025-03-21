# -*- coding: utf-8 -*-
import requests


def recognition_verifycode(url):
    """
    解析response返回的图片验证码
    :return:
    """

    r = requests.session()
    headers = {
        "": ""
    }

    response = r.get(url=url, headers=headers)
