############################################################
# Module  : Collect all data
# Date    : January 21st
# Author  : Xiao Ling
############################################################

from app import *

import re
import datetime

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 


############################################################
# Initialize application 
############################################################

root  = '/home1/l/lingxiao/xiao/good-great-ngrams/'
data  = os.path.join(root,'ngrams')

'''
   Ellie's data
'''
app_e = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'missing')

app_t = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-trans')

############################################################

app_e.refresh(2)
app_t.refresh(2)










