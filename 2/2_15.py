#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import brown
import nltk

count_of = {}
for genre in nltk.corpus.brown.categories():
    for word in brown.words(categories=genre):
        if word in count_of:
            count_of[word] = count_of[word] + 1
        else:
            count_of[word] = 1

for key, value in sorted(count_of.items(), key=lambda x:x[1]): #ラムダ式を用いることでsortする値をvalueに設定している
    if value >= 3:
        print "%s\t%d" % (key, value)
