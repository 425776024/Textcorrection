#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:40
# @Author  : xinfa.jiang
# @Site    : 
# @File    : util.py
# @Software: PyCharm

from functools import reduce
import pickle


def product(numbers: list = [0., 0.]) -> float:
    return reduce(lambda n1, n2: n1 * n2, numbers)


def load_pkl(path: str) -> any:
    with open(path, 'rb') as of:
        return pickle.load(of)


def save_pkl(path: str, obj: any) -> any:
    with open(path, 'wb') as of:
        return pickle.dump(obj, of)
