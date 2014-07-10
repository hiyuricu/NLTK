#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
from nltk.book import *

def vocab_size(t):
    return len(set(t))

if __name__ == "__main__":
  import sys
  vocab_size(sys.argv[1]) #input_file