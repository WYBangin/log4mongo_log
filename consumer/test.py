#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 17:05
# @Author  : 伯明
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Software: PyCharm
import sys
import requests
import json

sys.path.append("..")
from utils.common_utils import *


def start_barrage(test_id):
    """
    开启统计弹幕条数
    :param test_id: 直播ID
    :return:
    """
    logger.info("begin......")
    try:
        url = "http://127.0.0.1:5000/live_test?sid=" + str(test_id)
        response = requests.get(url)

        data = json.loads(response.text)
        return data
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    start_barrage("123")
