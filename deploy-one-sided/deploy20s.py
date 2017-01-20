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
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-20')

a21   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-21')

a22   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-22')

a23   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-23')


a24   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-24')


a25   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-25')

a26   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-26')

a27   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-27')

a28   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-28')

a29   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-29')

a30   = App(root
            ,data
            ,'one-sided-patterns'
            ,'two-sided-patterns'
            ,'/ellie/testset-30')

a20.refresh()
a21.refresh()
a22.refresh()
a23.refresh()
a24.refresh()
a25.refresh()
a26.refresh()
a27.refresh()
a28.refresh()
a29.refresh()
a30.refresh()


