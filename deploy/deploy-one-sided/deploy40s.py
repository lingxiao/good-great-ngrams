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

a40   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-40')

a41   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-41')

a42   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-42')

a43   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-43')

a44   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-44')


a45   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-45')

a46   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-46')

a47   = App(root
            ,data
            ,'outputs-2'
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'ellie/testset-47')


a40.refresh(1)
a41.refresh(1)
a42.refresh(1)
a43.refresh(1)
a44.refresh(1)
a45.refresh(1)
a46.refresh(1)
a47.refresh(1)


