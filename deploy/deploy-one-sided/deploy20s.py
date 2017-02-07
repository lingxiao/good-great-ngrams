############################################################
# Module  : Applicaton Main
# Date    : November 14th
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
from copy    import deepcopy

############################################################
# Initialize application 
############################################################

root  = '/home1/l/lingxiao/xiao/good-great-ngrams/'
data  = os.path.join(root, 'ngrams/')

a20   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-20')

a21   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-21')

a22   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-22')

a23   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-23')


a24   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-24')


a25   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-25')

a26   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-26')

a27   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-27')

a28   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-28')

a29   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-29')

a30   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-30')

a20.refresh(1)
a21.refresh(1)
a22.refresh(1)
a23.refresh(1)
a24.refresh(1)
a25.refresh(1)
a26.refresh(1)
a27.refresh(1)
a28.refresh(1)
a29.refresh(1)
a30.refresh(1)


