#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
from nltk.book import *

for t in [text1, text2, text3, text4, text5, text6, text7, text8, text9]:
    total_count = 0
    vocabulary1 = FreqDist(t).values()
    for i in range(0,len(set(t))):
        total_count += vocabulary1[i]
        if total_count * 100.0 / len(t) >= 33.3333333333333:
            print t, i + 1, total_count * 100.0 / len(t)
            break