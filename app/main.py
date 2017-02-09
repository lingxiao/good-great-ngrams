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

from PIL import Image

############################################################
# Initialize application 
############################################################


root   = "/Users/lingxiao/Documents/research/code/good-great-ngrams"
data   = os.path.join(root,'ngrams')

'''
   bansal's data
'''
app = App(root
         ,data
         ,'outputs-1'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-bansal')

'''
   Ellie's data
'''
app_e = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-ellie')

app_u = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'testset-ellie-unanimous')


two  = app_u.TwoSided
one  = app_u.OneSided

app_u.to_one_sided()

############################################################

tset = one.test()

prefix = 'ellie-unanimous-'


'''
  sanity check against bansal's data
bansal_rmarkov_ilp = markov_ilp(app)
bansal_rmilp       = milp      (app)
'''


'''
  ellie's data with unanimous ranking
'''
# rmarkov_ilp = markov_ilp(app_u)
rmilp       = milp      (app_u)

# app.save(prefix +  'markov-ilp', rmarkov_ilp)
app.save(prefix +  'milp'      , rmilp)












