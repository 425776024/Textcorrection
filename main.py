#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from src.ngram import Two_Gram
from tools.util import load_pkl

two_gram_counter = load_pkl('data/two_gram_counter.pkl')
two_gram_sum = load_pkl('data/two_gram_sum.pkl')

two_gram = Two_Gram(two_gram_counter, two_gram_sum)

# 给的，假设还可能是的；
print(two_gram.compare('游3D游戏发展5000多个点位', '梦幻西游3D游戏发展5000多个点位'))
