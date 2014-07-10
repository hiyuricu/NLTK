#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

def hedge(text):
    text = eval(text)
    i = 0
    for w in text:
        i += 1
        print w,
        if i == 3:
            print "like"
            i = 0

if __name__ == "__main__":
  import sys
  hedge(sys.argv[1]) #引数がリストのものに対応している