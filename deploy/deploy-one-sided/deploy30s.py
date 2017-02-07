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

a30   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-30')

a31   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-31')

a32   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-32')

a33   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-33')

a34   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-34')


a35   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-35')

a36   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-36')

a37   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-37')

a38   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-38')

a39   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-39')

a40   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-40')

a30.refresh(1)
a31.refresh(1)
a32.refresh(1)
a33.refresh(1)
a34.refresh(1)
a35.refresh(1)
a36.refresh(1)
a37.refresh(1)
a38.refresh(1)
a39.refresh(1)
a40.refresh(1)


