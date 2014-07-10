#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import nltk

from nltk.corpus import wordnet as wn

def supergloss(s):
    def defstring(a):
        return '[%s]: %s\n' % (a.name,  a.definition)

    definition = ''
    for hypernym in wn.synset(s).hypernyms():
        definition += defstring(hypernym)

    definition += '\n' + defstring(wn.synset(s)) + '\n'

    for hyponym in wn.synset(s).hyponyms():
        definition += defstring(hyponym)

    return definition

if __name__ == "__main__":
    print supergloss(sys.argv[1]) #argumentにはmotorcarのような任意の文字列を入れる