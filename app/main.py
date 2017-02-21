############################################################
# Module  : Applicaton Main
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

'''
   bansal's data
'''
app = App(root
         ,data
         ,'outputs-1'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-bansal')


'''
  CCB labels
'''
app_ccb = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'testset-ccb')

'''
  mohit's labels restricted
  to those that appear in veronica's graph
'''
app_moh = App(root
             ,data
             ,'outputs-2'
             ,'one-sided-patterns'
             ,'two-sided-patterns'
             ,'testset-bansal-in-graph')

app_all_moh = App(root
             ,data
             ,'outputs-2'
             ,'one-sided-patterns'
             ,'two-sided-patterns'
             ,'testset-moh-ppdb-words')

two  = app_all_moh.TwoSided
one  = app_all_moh.OneSided

app_ccb.to_one_sided()

############################################################
# app_all_moh.refresh()
# prefix = 'mohit-on-ppdb-graph-'

'''
  make n-gram graph 
'''

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


es = make_ngram_graph(app_all_moh, os.path.join(root, 'ngram-graph.txt'))

# a,b = pwords[0]
# a,b  = 'ill','old'


'''
  test mohit's stuff on subset of 
  words that also appear on ppdb graph
'''
# rmarkov_ilp = markov_ilp(app_moh)
# rmilp       = milp      (app_moh)

# app.save(prefix +  'markov-ilp', rmarkov_ilp)
# app.save(prefix +  'milp'      , rmilp)

# '''
#   sanity check against bansal's data
# '''

# bansal_rmarkov_ilp = markov_ilp(app)
# bansal_rmilp       = milp      (app)

# print ('=== bansal milp: ', bansal_rmilp      ['average'])
# print ('=== bansal  ilp: ', bansal_rmarkov_ilp['average'])


''' 
  Collect all the negative taus
milp_negative = []
ilp_negative  = []

for d in rmilp['ranking']:
  if d['tau'] < 0:
    milp_negative.append(d)

for d in rmarkov_ilp['ranking']:
  if d['tau'] < 0:
    ilp_negative.append(d)

rilp_positive = [d for d in rmarkov_ilp['ranking'] if d not in ilp_negative ]
milp_positive = [d for d in rmilp['ranking']       if d not in milp_negative]

milp_negative_gold = [d['gold'] for d in milp_negative]
ilp_negative_gold  = [d['gold'] for d in rilp_negative]

milp_positive_gold = [d['gold'] for d in milp_positive]
ilp_positive_gold  = [d['gold'] for d in rilp_positive]

f_milp_positive = open(os.path.join(root, 'milp-positive.txt'),'w')
f_ilp_positive  = open(os.path.join(root, 'ilp-positive.txt') ,'w')

f_milp_negative = open(os.path.join(root, 'milp-negative.txt'),'w')
f_ilp_negative  = open(os.path.join(root, 'ilp-negative.txt') ,'w')


for gold in milp_positive_gold:
  ws = [w for [w] in gold]
  f_milp_positive.write('=== ' + ws[0] + ', ' + ws[-1] + ' **\n')
  for w in ws:
    f_milp_positive.write(w + '\n')

f_milp_positive.write('=== END')


for gold in ilp_positive_gold:
  ws = [w for [w] in gold]
  f_ilp_positive.write('=== ' + ws[0] + ', ' + ws[-1] + ' **\n')
  for w in ws:
    f_ilp_positive.write(w + '\n')

f_ilp_positive.write('=== END')


for gold in ilp_negative_gold:
  ws = [w for [w] in gold]
  f_ilp_negative.write('=== ' + ws[0] + ', ' + ws[-1] + ' **\n')

  for w in ws:
    f_ilp_negative.write(w + '\n')

f_ilp_negative.write('=== END')


for gold in milp_negative_gold:
  ws = [w for [w] in gold]
  f_milp_negative.write('=== ' + ws[0] + ', ' + ws[-1] + ' **\n')

  for w in ws:
    f_milp_negative.write(w + '\n')

f_milp_negative.write('=== END')

f_milp_positive.close()  
f_milp_negative.close()

f_ilp_positive.close()  
f_ilp_negative.close()



'''

'''
  open all files from outputs-1 and save into output-2
'''

# ipath = '/Users/lingxiao/Desktop/remote-2-sided'
# # ipath = os.path.join(root,'outputs-1/two-sided-patterns')
# opath = os.path.join(root,'outputs-2/two-sided-patterns')

# files = os.listdir(ipath)

# # for f in files:

# #   hi = os.path.join(ipath,f)
# #   xi = open(hi,'r').read()
# #   ho = os.path.join(opath,f)
# #   xo = open(ho,'w')
# #   xo.write(xi)
# #   xo.close()

































