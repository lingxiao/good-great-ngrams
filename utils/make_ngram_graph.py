############################################################
# Module  : make ngram graph
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import os

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 


'''
  @Use: make graph over all WxW words in mohit's data
'''
def make_ngram_graph(app, outpath):

  outpath = os.path.join(root, 'ngram-graph.txt')

  two    = app.TwoSided
  words  = join(join([t for _,_,t in two.test()]))
  edges  = dict()

  for a in words:
    for b in words:
      if (a,b) in edges or (b,a) in edges: pass
      else: 
        d_ab = two.data(a,b)
        d_ba = two.data(b,a)

        a_stronger_b = [n for _, n in d_ab['strong-weak'] + d_ba['weak-strong']]
        b_stronger_a = [n for _, n in d_ab['weak-strong'] + d_ba['strong-weak']]

        ab_strong_edge = [(b,a,'is weaker than') for _ in range(int(sum(a_stronger_b)))]
        ab_weak_edge   = [(a,b,'is weaker than') for _ in range(int(sum(b_stronger_a)))]

        edges[(a,b)] = ab_strong_edge + ab_weak_edge

  f = open(outpath,'w')

  for _,es in edges.iteritems():
    for a,b,v in es:
      f.write(a + ',' + b + ',' + v + '\n')
  f.close()

  return edges


