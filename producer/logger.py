#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:26
# @Author  : 伯明
# @Site    : 
# @File    : logger.py.py
# @Software: PyCharm
# -*- encoding:utf-8 -*-
import sys
import logging

sys.path.append("..")
from common.config import *
from log4mongo.handlers import MongoHandler

logger = logging.getLogger(APP_NAME)

mon = MongoHandler(host=MONGO_HOST, database_name=MONGO_DB)
mon.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(mon)
logger.addHandler(ch)
