#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk

def find_top50(input_file):
    input_file = eval(input_file) #evalは文字列を式として評価する関数。万能だが入力側に権限を与えてしまうためあまり使わない方が良い。
    bi = nltk.bigrams(nltk.Text(input_file))
    stopwords = nltk.corpus.stopwords.words('english')
    count_of = {}
    for tuple in bi:
        if tuple[0].lower() not in stopwords and tuple[1].lower() not in stopwords:
            if tuple in count_of:
                count_of[tuple] = count_of[tuple] + 1
            else:
                count_of[tuple] = 1

    i = 0
    for k, v in sorted(count_of.items(), key=lambda x:x[1], reverse=True):
        if i < 50:
            print "%s %s" % (k, v)
            i += 1
        else:
            break

if __name__ == "__main__":
  import sys
  find_top50(sys.argv[1]) #input_file