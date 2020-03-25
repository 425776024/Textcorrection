#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 13:40
# @Author  : xinfa.jiang
# @Site    : 
# @File    : ngram.py
# @Software: PyCharm
from tools.cut_data import cut
from tools.util import product


class Two_Gram:
    def __init__(self, two_gram_counter, two_gram_sum):
        # self.words_count = words_count
        # self.sum_frequence = sum_frequence

        self.two_gram_counter = two_gram_counter
        self.two_gram_sum = two_gram_sum

    def get_2_prob(self, w1, w2: str) -> float:
        return (self.two_gram_counter[w1 + w2] + 1) / self.two_gram_sum

    #
    # def get_prob(self, word: str) -> float:
    #     return (self.words_count[word] + 1) / self.sum_frequence

    def call(self, sentence: str) -> float:
        sentence_probability = 0
        words = cut(sentence)
        for i, word in enumerate(words):
            if i == 0:
                continue
            else:
                pre_word = words[i - 1]
                prob = self.get_2_prob(pre_word, word)
            sentence_probability += prob
        s = sentence_probability / (len(words) - 1)
        return s

    def compare(self, s1: str, s2: str) -> str:
        score1 = self.call(s1)
        score2 = self.call(s2)
        return s1 if score1 > score2 else s2
