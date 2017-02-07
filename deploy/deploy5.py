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

a1    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-1')

a2    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-2')

a3    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-3')

a4    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-4')

a5    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'ellie-unanimous/testset-5')

a1.refresh(1)
a2.refresh(1)
a3.refresh(1)
a4.refresh(1)
a5.refresh(1)




