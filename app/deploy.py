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
data   = "/Users/lingxiao/Documents/research/data/ngrams/"

# app2   = App(root
#             ,data
#             ,'one-sided-patterns'
#             ,'two-sided-patterns'
#             ,'/ellie/testset-2')

# collecting bansal data for check
app4   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-4')

# app5   = App(root
#             ,data
#             ,'one-sided-patterns'
#             ,'two-sided-patterns'
#             ,'/ellie/testset-5')


app6   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-6')

############################################################
# will run next roud


app7   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-7')
