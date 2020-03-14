#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 17:42
# @Author  : 伯明
# @Site    : 
# @File    : mongo_conf.py
# @Software: PyCharm

CONFIG = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'mongo': {
            'class': 'log4mongo.handlers.MongoHandler',
            'host': 'localhost',
            # 'port': 27017,
            'database_name': 'mongo_logs2',
            # 'collection': 'logs',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            # 'propagate': True,
        },
        'simple': {
            'handlers': ['console', 'file'],
            'level': 'WARN',
        },
        'mongo': {
            'handlers': ['console', 'mongo'],
            'level': 'DEBUG',
        }
    }
}
