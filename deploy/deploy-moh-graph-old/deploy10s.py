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


a6    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-6')

a7    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-7')

a8    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-8')


a9    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-9')


a10    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'moh-graph/testset-10')


a10.refresh(2)
a9.refresh(2)
a8.refresh(2)
a7.refresh(2)
a6.refresh(2)
