#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import nltk

from nltk.corpus import wordnet as wn

total, count = 0, 0
for syn in wn.all_synsets('n'):
    if syn.hyponyms() == []:
        count += 1
    total += 1

print '%d/%d' % (count, total)