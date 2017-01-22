############################################################
# Module  : Applicaton Main
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import os
import re
import datetime

from pulp import *
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
data   = os.path.join(root,'ngrams')

app = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-bansal')



app_e = App(root
         ,data
         ,'outputs-1'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-ellie')

app_t = App(root
         ,data
         ,'outputs-1'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-trans')

app_d = App(root
         ,data
         ,'outputs-1'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-ellie-has-data')

two  = app_e.TwoSided
one  = app_e.OneSided

############################################################




############################################################
# run all experiments

# app.to_one_sided()

# prefix = 'ellie_'

# rmilp          = milp(app_d)
# app.save(prefix + 'milp-has-data', rmilp)

# rmilpt         = milp(app_t)
# app_t.save(prefix + 'milp-trans', rmilpt)


# rmarkov_abs    = markov_absolute(app)
# app.save(prefix + 'markov-heuristic', rmarkov_abs)

# rmarkov_derive = markov_derive(app)
# app.save(prefix +  'markov-pairwise-approx', rmarkov_derive)

# rmarkov_ilp    = markov_ilp(app_e)
# print (rmarkov_ilp['average'])
# app.save(prefix + 'markov-ilp', rmarkov_ilp)

# rmarkov_milp   = markov_milp(app)
# app.save(prefix + 'markov-milp', rmarkov_milp)

# test = two.test()












