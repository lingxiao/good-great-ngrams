############################################################
# Module  : My formulation of ILP
# Date    : December 10th
# Author  : Xiao Ling
############################################################

from pulp    import *
from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 
 
def markov_ilp(app):

  one     = app.OneSided
  two     = app.TwoSided
  ranking = [ilp_each(gold,one,two) for _,_,gold in one.test()]

  taus      = [r['tau']             for r in ranking]
  taus2     = [r['tau-notie']       for r in ranking]
  pairs     = [r['pairwise']        for r in ranking]

  avg_tau      = sum(taus)                  / len(taus)
  avg_abs_tau  = sum(abs(t) for t in taus)  / len(taus)
  avg_tau2     = sum(taus2)                 / len(taus2)
  avg_abs_tau2 = sum(abs(t) for t in taus2) / len(taus2)
  avg_pair     = sum(pairs)                 / len(pairs)

  return {'ranking' : ranking
         ,'pattern' : one.pattern()
         ,'average' : {'tau'                 : avg_tau
                      ,'tau-notie'           : avg_tau2
                      ,'absolute-tau'        : avg_abs_tau
                      ,'absolute-tau-no-tie' : avg_abs_tau2
                      ,'pair-wise'           : avg_pair }  
         }

def ilp_each(gold,one,two):

  words   = join(gold)

  for k in range(0,10):
    shuffle(words)


  '''
    construct variables
  '''
  # pairs   = unique_pairs(words)
  pairs   = [(u,v) for u in words for v in words if u != v]

  triples = [(u,v,w) for u in words for v in words for w in words
          if u != v and v != w and u != w]

    
  '''
    get probs and construct score
  '''
  probs  = [rank_pairwise(one,two,u,v) for u,v in pairs]
  score  = dict()
  eps    = 10-7

  for d in probs:
    [(uv,p_uv),(vu,p_vu)] = [(k,v) for k,v in d.iteritems() if k != 'rank']

    Z         = p_uv + p_vu  + eps
    score[uv] = (p_uv + eps)/Z
    score[vu] = (p_vu + eps)/Z

  '''
    construct milp solver
  '''
  prob =  LpProblem ('='.join(words), LpMaximize)


  '''
    variables where u-v imples u > v
  ''' 
  variables = dict()

  for u,v in pairs:
    uv = u +'='+ v
    variables[uv] = LpVariable('s_' + uv, 0,1, LpInteger)

  '''
    objective function
  '''
  objective = [ score[u+' > '+v]     *      variables[u+'='+v]  \
              for u,v in pairs] \
            + [ score[v + ' > '+  u] * (1 - variables[u+'='+v]) \
              for u,v in pairs]


  prob += lpSum(objective)  


  # constraints
  for i,j,k in triples:
    prob += (1 - variables[i + '=' + j]) \
         +  (1 - variables[j + '=' + k]) \
         >= (1 - variables[i + '=' + k])


  prob.solve()

  '''
    output ranking
  '''
  algo = prob_to_algo_rank(prob,words)

  return {'gold'          : gold
         ,'algo'          : algo
         ,'tau'           : tau (gold,algo)
         ,'tau-max'       : tau (gold,gold)   # need this since max tau not necessarily 1.0
         ,'tau-notie'     : tau2(gold,algo)
         ,'tau-notie-max' : tau2(gold,gold)
         ,'pairwise'      : pairwise_accuracy(gold,algo)
         ,'raw-score'     : score
         ,'raw-stat'      : []
         }

############################################################
# Output ranking in list form

def to_rank(raw,words):

  # construct graph :: dictionary for topological sort
  order = dict()        
  for s,w in raw:
    if s in order:
      order[s] += [w]
    else:
      order[s] = [w]

  # complete the sink in the dictonary
  for w in words:
    if w not in order: order[w] = []

  return [[w] for w in toposort(order)]




  






