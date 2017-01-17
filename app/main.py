############################################################
# Module  : Applicaton Main
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import re
import datetime
from pulp    import *

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 
from copy    import deepcopy

############################################################
# Initialize application 
############################################################

root   = "/Users/lingxiao/Documents/research/code/good-great"
# data   = "/Users/lingxiao/Documents/research/data/ngrams/"
data   = os.path.join(root, 'ngrams/')

app    = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'testset')

ngram  = app.NGRAM
one    = app.OneSided
two    = app.TwoSided

app.to_one_sided()

# read_test :: FilePath -> IO [String]
# def read_test(path):

# path  = '/Users/lingxiao/Documents/research/code/good-great/inputs/testset.txt'

# raw = [r for r in open(path,'r').read().split('=== ') if r]
# raw = [r.split('\n')[0:-1] for r in raw]
# raw = [r for r in raw if r][0:-1]

# test = []

# for xs in raw:
# 	u,v = xs[0].split(', ')
# 	ys  = [x.split(', ') for x in xs[1:]]
# 	test.append((u,v,ys))

############################################################
# run all experiments

prefix = 'veronica_'

# rmilp          = milp(app)
# app.save(prefix + 'milp-syn', rmilp)

# rmarkov_abs    = markov_absolute(app)
# app.save(prefix + 'markov-heuristic', rmarkov_abs)

# rmarkov_derive = markov_derive(app)
# app.save(prefix +  'markov-pairwise-approx', rmarkov_derive)

# rmarkov_ilp    = markov_ilp(app)
# print (rmarkov_ilp['average'])
# app.save(prefix + 'markov-ilp', rmarkov_ilp)

# rmarkov_milp   = markov_milp(app)
# app.save(prefix + 'markov-milp', rmarkov_milp)










