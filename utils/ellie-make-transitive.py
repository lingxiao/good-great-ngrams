############################################################
# Module  : make ellie's labels transitive if possible
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import os
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

root   = "/Users/lingxiao/Documents/research/code/good-great-ngrams"
data   = os.path.join(root,'ngrams')

app = App(root,data, 'one-sided-patterns','two-sided-patterns', '/testset')

two  = app.TwoSided
tset = two.test()


def complete(xss):

      yss = []

      for xs in xss:
            if len(xs) == 1:
                  u,v = xs[0]
            else:
                  u,_ = xs[0]
                  _,v = xs[-1]

            pre_u  = [rs for rs in foo if rs[-1][-1] == u]
            post_v = [rs for rs in foo if rs[0][0]   == v]
            yss.append(join(pre_u + [xs] + post_v))

      return yss


def complete_under_endpoint(xss):
      xss1 = complete(xss)
      if xss1 != xss: 
            return complete_under_endpoint(xss1)
      else: 
            yss = []
            for xs in xss1:
                  if xs not in yss: yss.append(xs)
            return yss

def shrink(xs): 
    u,v = xs [0]
    return [[u],[v]] + [[v] for _,v in xs[1:]]


tset1 = [[(u,v)] for _,_,[[u],[v]] in tset]
tset2 = complete_under_endpoint(tset1)
tlong = [t for t in tset2 if len(t) > 2]

save  = [shrink(t) for t in tlong]

f = open(os.path.join(root,'transitive-test.txt'),'w')

for xs in save:
    f.write('=== foo, bar **\n')
    for [x] in xs:
        f.write(x + '\n')
f.write('=== END')        
f.close()    






