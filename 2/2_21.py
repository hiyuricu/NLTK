#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from nltk.corpus import brown, cmudict

def count_syllable(genre):
    src = cmudict.dict()
    syllable_count = 0
    word_count = 0
    undefined_word = 0
    for word in brown.words(categories=genre):
        temp_count = 0
        defined_word = 0
        word_count += 1
        if word in src:
            #print word, src[word], len(src[word][0])
            for element in src[word]:
                defined_word += 1
                temp_count += len(element)
            syllable_count += float(temp_count) / defined_word
        else:
            undefined_word += 1

    average_syllable = float(syllable_count) / (word_count - undefined_word)
    syllable_count = syllable_count + undefined_word * average_syllable
    return syllable_count

if __name__ == "__main__":
    print count_syllable(sys.argv[1]) #ブラウンコーパスのジャンルを入力してもらう

#単語をlower_caseしないといけないかも