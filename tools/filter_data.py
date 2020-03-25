#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:37
# @Author  : xinfa.jiang
# @Site    : 
# @File    : filter_data.py
# @Software: PyCharm
import re


# 只保留正常中文、字母单词、数字
def token(string):
    try:
        if string is not None or str(string) != 'nan':
            return ' '.join(re.findall('[\w|\d]+', string))
    except:
        return ''
