#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
from nltk.book import text6

listize = []
listz = []
listpt = []
listtitlecase = []

for word in text6:
    if word.endswith("ize"):
        listize.append(word)

    if "z" in word:
        listz.append(word)

    if "pt" in word:
        listpt.append(word)

    if word.istitle():
        listtitlecase.append(word)

print listize
print listz
print listpt
print listtitlecase