#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 14:59
# @Author  : xinfa.jiang
# @Site    : 
# @File    : data_process.py
# @Software: PyCharm

import pandas as pd
from tools.cut_data import cut
from collections import Counter
from tools.util import save_pkl

path = 'data/SmoothNLP.csv'
dataf = pd.read_csv(path, sep='\t')
dataf.dropna(inplace=True)

all_lines = dataf['title'].tolist() + dataf['content'].tolist()
TEXT = ''.join(all_lines)

ALL_TOKENS = cut(TEXT)

FILTER_TOKENS = [ti for ti in ALL_TOKENS if ti.strip() != '' and ti != 'n']

# 连续的两个词，2-gram
all_2_gram_words = [''.join(FILTER_TOKENS[i:i + 2]) for i in range(len(FILTER_TOKENS) - 2)]

# 连续的两个词的词频
two_gram_counter = Counter(all_2_gram_words)

two_gram_sum = sum([f for w, f in two_gram_counter.most_common()])
save_pkl('data/two_gram_counter.pkl', two_gram_counter)
save_pkl('data/two_gram_sum.pkl', two_gram_sum)
print(two_gram_sum)
