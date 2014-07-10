#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import brown
import nltk

print '    Genre    \tTokens\tTypes\tLexical diversity'

for genre in nltk.corpus.brown.categories():
    words = brown.words(categories=genre)
    cnt = float(len(words))
    word_cnt = len(set(words))
    print '%s\t%6d\t%5d\t%10.2f' % (genre.center(13), cnt, word_cnt, cnt / word_cnt)