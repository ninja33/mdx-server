# -*- coding: utf-8 -*-
# version: python 2.7

from pattern.en import lemma
import sys

if __name__=="__main__":
    if len(sys.argv) < 1 :
        print "lemma.py word"
        exit(0)
    word=sys.argv[1]
    print lemma(word)
