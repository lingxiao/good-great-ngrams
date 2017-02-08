############################################################
# Module  : Applicaton Main
# Date    : November 14th
# Author  : Xiao Ling
############################################################

import os
import re
import datetime

from pulp import *
from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 
from copy    import deepcopy

from PIL import Image

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
   Ellie's data
'''
app_e = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         # , 'ellie/testset-6')
         , 'testset-ellie')

app_t = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-trans')

app_d = App(root
         ,data
         ,'outputs-2'
         ,'one-sided-patterns'
         ,'two-sided-patterns'
         , 'testset-ellie-has-two-data')

app_d2 = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'testset-has-data-one-sided')

app_u = App(root
           ,data
           ,'outputs-2'
           ,'one-sided-patterns'
           ,'two-sided-patterns'
           ,'testset-ellie-unanimous')


two  = app_u.TwoSided
one  = app_u.OneSided

app_u.to_one_sided()

############################################################


# path   = '/Users/lingxiao/Documents/research/code/good-great-ngrams/outputs-2/one-sided-patterns'
# files  = os.listdir(path)
# files1 = [f.replace('.txt','') + '-1' + '.txt' for f in files] 

# paths = [os.path.join(path,f) for f in files]

# no_content = []

# for p in paths:
#   f = open(p,'r').read()
#   if not f:
#     no_content.append(p)
#     os.remove(p)
#     print ('removing ' + p)




# yes = [f1 for f1 in files1 if f1 in files]

# yes = []

# for f1 in files1:
#   if f1 in files:
#     yes.append(f1)
#     print f1
#   else:
#     print 'no'






# m_absolute = markov_absolute(app_u)

# prefix = 'ellie'
# rmarkov_ilp    = markov_ilp     (app_u)
# rmarkov_abs    = markov_absolute(app_u)

# print (rmarkov_ilp['average'])
# app.save(prefix + 'markov-ilp', rmarkov_ilp)


# milp_e = milp(app_e)

# rmilpt         = milp(app_t)
# app_t.save(prefix + 'milp-trans', rmilpt)

# app.save(prefix + 'markov-heuristic', rmarkov_abs)

# rmarkov_derive = markov_derive(app_u)
# app.save(prefix +  'markov-pairwise-approx', rmarkov_derive)

# rmarkov_ilp    = markov_ilp(app_e)
# print (rmarkov_ilp['average'])
# app.save(prefix + 'markov-ilp', rmarkov_ilp)

# rmarkov_milp   = markov_milp(app)
# app.save(prefix + 'markov-milp', rmarkov_milp)

'''
  Collect patterns for remaining words
test = one.test()
name = 'testset'

k    = 1

words = list(chunks(test,10))

for word_set in words:
  if word_set:
    p = os.path.join(root, name + '-' + str(k) + '.txt')
    f = open(p,'w')

    for u,v,xs in word_set:
      f.write('=== ' + u + ', ' + v + '\n')
      for [x] in xs:
        f.write(x + '\n')
    f.write('=== END')
    k += 1
'''  



'''
  test = two.test()

  not_zero = []

  words = list(set(join([u,v] for _,_,[[u],[v]] in tset)))

  for word in words:
    d = one.data(word)
    s = [n for _,n in d['strong']]
    w = [n for _,n in d['weak']]
    if None not in s and None not in w:
      if sum(s) or sum(w): 
        not_zero.append(word)

  not_zero_pairs = [(u,v) for _,_,[[u],[v]] in tset if u in not_zero and v in not_zero]      

  f = open(os.path.join(root,'inputs/testset-has-data-one-sided.txt'),'w')

  for u,v in not_zero_pairs:
     f.write('=== foo, bar **\n')
     f.write(u + '\n')
     f.write(v + '\n')
  f.write('=== END')   
  f.close()

'''

'''

not_zero = []

for _,_,[[u],[v]] in tset:
   d = one.data(u,v)
     s = [n for _,n in d['strong-weak']]
     w = [n for _,n in d['weak-strong']]

     if None not in s and None not in w:
        if sum(s) or sum(w): not_zero.append((u,v))

f = open(os.path.join(root,'has-data.txt'),'w')

for u,v in not_zero:
   f.write('=== foo, bar **\n')
   f.write(u + '\n')
   f.write(v + '\n')
f.write('=== END')   
f.close()

'''

'''
  fix images in outputs-2/two-sided-patterns
  p_current = '/Users/lingxiao/Documents/research/code/good-great-ngrams/outputs-2/two-sided-patterns'
  # p_current = '/Users/lingxiao/Documents/research/code/good-great-ngrams/temp'
  p_old     = p_current + '-old'


  old_files = os.listdir(p_current)


  # for f in old_files:
  #   pold  = os.path.join(p_old    ,f)
  #   pcurr = os.path.join(p_current,f)
  #   po = open(pold,'r').read()
  #   print (po)
  #   pn = open(pcurr,'w').write(po)

'''












