############################################################
# Module  : Applicaton Main
# Date    : November 14th
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


a26    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-26')

a27    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-27')

a28    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-28')


a29    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-29')


a30    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-30')


a31    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-31')


a32    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-32')

a26.refresh(2)
a27.refresh(2)
a28.refresh(2)
a29.refresh(2)
a30.refresh(2)
a31.refresh(2)
a32.refresh(2)
