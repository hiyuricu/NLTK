#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import brown
from nltk.book import *

def word_freq(target_word, genre):
    fdist = FreqDist(brown.words(categories=genre))
    print ("genre = %s, target_word = %s, frequency = %d") % (genre, target_word, fdist[target_word])

if __name__ == "__main__":
  import sys
  word_freq(sys.argv[1], sys.argv[2])