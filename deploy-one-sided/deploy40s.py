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
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-40')

a41   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-41')

a42   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-42')

a43   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-43')

a44   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-44')


a45   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-45')

a46   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-46')

a47   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-47')


a40.refresh()
a41.refresh()
a42.refresh()
a43.refresh()
a44.refresh()
a45.refresh()
a46.refresh()
a47.refresh()


