############################################################
# Module  : rank
# Date    : December 10th
# Author  : Xiao Ling
############################################################

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 


############################################################
'''
  @Use: given milp object, output ranking
        as list of lists

  prob_to_algo_rank :: MILP -> [[String]] -> [[String]]
'''  
def prob_to_algo_rank(prob,words):

  '''
    interpret score as ranking
  '''
  raw0 = [tuple(v.name.split('_'))                    
          for v in prob.variables() if v.varValue == 1.0]

  '''
    words of form wo-rd need to be taken care of
  # '''

  raw1 = []

  for t in raw0:

    if len(t) == 2: 

      (x,uv) = t
      [u,v]  = uv.split('=')
      raw1.append((x,u,v))

    elif len(t) == 3:

      (x,u,v) = t

      if '=' in u:
        [word1,word2a] = u.split('=')
        raw1.append((x, word1, word2a + '-' + v))
      elif '=' in v:
        [word1b,word2] = v.split('=')
        raw1.append((x, u + '-' + word1b, word2))

  # if we have s_ij and w_ij, then we have a contradiction
  contradiction = [(s,u,v)                  \
                  for (s,u,v) in raw1       \
                  for (w,u1,v1) in raw1     \
                  if s == 's' and w == 'w'  \
                  and u == u1 and v == v1]

  raw  = [(u,v) for (x,u,v) in raw1 if x == 's']

  # # construct graph :: dictionary for topological sort
  order = dict()        

  for s,w in raw:
    if s in order:
      order[s] += [w]
    else:
      order[s] = [w]

  # complete the sink in the dictonary
  for w in words:
    if w not in order: order[w] = []

  algo = [[w] for w in toposort(order)]


  return algo

