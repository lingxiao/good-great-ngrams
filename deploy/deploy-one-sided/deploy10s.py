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
            ,'ellie/testset-1')

a2   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-2')

a3   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-3')

a4   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-4')

a5   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-5')


a6   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-6')

a7   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-7')

a8   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-8')

a9   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-9')

a10   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-10')


a1.to_one_sided()

a1.refresh(1)
a2.refresh(1)
a3.refresh(1)
a4.refresh(1)
a5.refresh(1)
a6.refresh(1)
a7.refresh(1)
a8.refresh(1)
a9.refresh(1)
a10.refresh(1)


