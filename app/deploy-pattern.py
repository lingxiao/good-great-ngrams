############################################################
# Module  : Applicaton Main
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import os
import re
import datetime

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 
from copy    import deepcopy

############################################################
# Initialize application 
############################################################


current = os.getcwd()
root    = os.path.abspath(os.path.join(current, os.pardir))
data    = os.path.join(root, 'ngrams/')

app    = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'testset')

ngram  = app.NGRAM
one    = app.OneSided
two    = app.TwoSided

app.to_one_sided()

############################################################
# run all experiments

prefix = 'veronica_'

'''
    Collect patterns without going through the server
'''
patterns = two.pattern()

path  = os.path.join(data,'grepped/grepped-data')
paths = fmap(lambda x : os.path.join(path, x), os.listdir(path)[1:])

ps = parse_pattern(patterns['weak-strong'],['good','great'])

def run(path, words):

    with open(path, 'r') as f:

        for line in f:

            xs  = line.split('\t')

            if len(xs) == 2:
                [t,n] = xs
                n     = float(n.replace('\n',''))

                for w in words:
                    if t == w: words[w].append((t,n))


    for w,ret in words.iteritems():
        print ('======= ' + w + '======= \n')
        print (ret)
        one.write_word(w,ret)





