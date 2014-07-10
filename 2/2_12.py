#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import nltk

entries = nltk.corpus.cmudict.entries()
before_word = ""
temp_word = 0
temp_list = []
multiple_pronounce_count = 0

for entry in entries:
    if before_word == entry[0]:
        temp_word += 1
        if temp_word == 1:
            multiple_pronounce_count += 1

    else:
        if len(temp_list) > 1:
            print temp_list
        temp_word = 0
        temp_list = []
    temp_list.append(entry)
    before_word = entry[0]

print multiple_pronounce_count, len(entries)