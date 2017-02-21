############################################################
# Module  : Applicaton Main
# Date    : November 24th
# Author  : Xiao Ling
############################################################

from app import *

from prelude import * 
from utils   import *
from server  import * 
from client  import * 

############################################################
# Initialize application 
############################################################

# root  = '/home1/l/lingxiao/xiao/good-great-ngrams/'
root  = "/Users/lingxiao/Documents/research/code/good-great-ngrams"
data  = os.path.join(root, 'ngrams/')


a24    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-24')


a24.refresh(2)
