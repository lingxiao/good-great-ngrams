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

############################################################
# Module  : Applicaton Main
# Date    : November 14th
# Author  : Xiao Ling
############################################################

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

root   = "/Users/lingxiao/Documents/research/code/good-great-ngrams"
data   = "/Users/lingxiao/Documents/research/data/ngrams/"



app36   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-36')


app35   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-35')

app34   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-34')

app33   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-33')

app32   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-32')





app37   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-37')

app31   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-31')


app30   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-30')


app29   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-29')


app28   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-28')


app27   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-27')


app26   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-26')

# app.to_one_sided()

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










