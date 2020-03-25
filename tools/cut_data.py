#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:37
# @Author  : xinfa.jiang
# @Site    : 
# @File    : cut_data.py
# @Software: PyCharm

import jieba

jieba.load_userdict('data/user_dict.txt')
def cut(string):
    return list(jieba.cut(string))
