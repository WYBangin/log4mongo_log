#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 15:05
# @Author  : 伯明
# @Site    : 
# @File    : common_utils.py
# @Software: PyCharm
import sys
import os

sys.path.append("..")
import time
import socket
from datetime import datetime, timedelta, timezone
from producer.logger import *
from pipeline.connect import Logs
from common.config import *


def show_error_function(func):
    """展示报错信息的函数"""

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return logger.error("this is error log:{}".format(e))

    return wrapper


def count_request_time(func, *args, **kwargs):
    """统计请求花费时间的装饰器 (单位：毫秒)"""

    begin_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    request_time = int(round(end_time - begin_time, 3) * 1000)
    print("花费{}ms".format(request_time))
    return request_time


def get_host_ip():
    """获取主机IP方法的函数"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def utc_change():
    """格林时间转换的函数"""
    utc_tz = timezone.utc
    beijing = timezone(timedelta(hours=8))
    utc_time = datetime.utcnow().replace(tzinfo=utc_tz)
    utc_beijing = utc_time.astimezone(beijing).replace(microsecond=0).isoformat()
    return utc_beijing


def write_log(message, logger_name, port, log_type, level, thread_name):
    cur_host = get_host_ip()
    cur_time = datetime.now()
    db_obj = Logs(app_name=APP_NAME, logger_name=logger_name, host=cur_host, port=port, type=log_type, level=level,
                  thread_name=thread_name, message=message, write_time=cur_time)
    db_obj.save()

