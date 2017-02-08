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


a21    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-21')

a22    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-22')

a23    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-23')


a21.refresh(2)
a22.refresh(2)
a23.refresh(2)

