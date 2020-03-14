#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 14:57
# @Author  : 伯明
# @Site    : 
# @File    : connect.py
# @Software: PyCharm
import sys
import os

sys.path.append("..")
from mongoengine import *

from common.config import *
from datetime import datetime

connect(MONGO_DB, host=MONGO_HOST, port=MONGO_PORT)


class Logs(Document):
    """日志集合字段"""
    app_name = StringField(required=True, max_length=200)  # 应用名/模块名
    logger_name = StringField(required=True, max_length=200)  # 日志名
    host = StringField(required=True, default="127.0.0.1", max_length=50)  # 主机名
    port = IntField(required=True, default=os.getpid())  # 运行程序的进程号/线程号
    type = StringField(required=True, default="syslog")  # 日志类型, 默认系统日志
    level = StringField(required=True, default="info")
    thread_name = StringField(required=True, max_length=200)  # 线程名
    message = StringField(required=True, max_length=5000)  # 日志内容
    write_time = DateTimeField(default=datetime.now)  # 写入时间
    create_time = DateTimeField(default=datetime.now)    # 当前创建时间
