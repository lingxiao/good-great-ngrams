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

root  = "/Users/lingxiao/Documents/research/code/good-great-ngrams"
data  = os.path.join(root, 'ngrams/')

a    = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'testset-moh-ppdb-words')


a.refresh(2)
