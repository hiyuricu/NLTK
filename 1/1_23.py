#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
from nltk.book import text6

for w in text6:
    if w.isupper():
        print w
