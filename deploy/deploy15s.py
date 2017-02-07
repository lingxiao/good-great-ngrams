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

root  = '/home1/l/lingxiao/xiao/good-great-ngrams/'
data  = os.path.join(root, 'ngrams/')



a11    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-11')


a12    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-12')


a13    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-13')

a14    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-14')


a15    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-15')


a11.refresh(1)
a12.refresh(1)
a13.refresh(1)
a14.refresh(1)
a15.refresh(1)