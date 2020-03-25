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

words_count = Counter(FILTER_TOKENS)
sum_frequence = sum([f for w, f in words_count.most_common()])

save_pkl('data/words_count.pkl', words_count)
save_pkl('data/sum_frequence.pkl', sum_frequence)
print(sum_frequence)
