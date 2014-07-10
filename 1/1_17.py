#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
from nltk.book import text9

for i in range(0,text9.index("sunset")):
    if text9[i] == ".":
        sentence_zero_number = i

for i in range(text9.index("sunset"),len(text9)):
    if text9[i] == ".":
        sentence_last_number = i
        break

print " ".join(text9[sentence_zero_number + 1:sentence_last_number + 1])