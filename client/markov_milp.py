############################################################
# Module  :
# Date    : December 10th
# Author  : Xiao Ling
############################################################

from pulp    import *
from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 
from nltk.corpus import wordnet as wn


############################################################
# All

def markov_milp(app):
  
  two       = app.TwoSided
  ranking   = [milp_no_syn(gold,app) for _,_,gold in two.test()]

  taus      = [r['tau']             for r in ranking]
  taus2     = [r['tau-notie']       for r in ranking]
  pairs     = [r['pairwise']        for r in ranking]

  avg_tau      = sum(taus)                  / len(taus)
  avg_abs_tau  = sum(abs(t) for t in taus)  / len(taus)
  avg_tau2     = sum(taus2)                 / len(taus2)
  avg_abs_tau2 = sum(abs(t) for t in taus2) / len(taus2)
  avg_pair     = sum(pairs)                 /len(pairs)


  return {'ranking' : ranking
         ,'pattern' : two.pattern()
         ,'average' : {'tau'                 : avg_tau
                      ,'tau-notie'           : avg_tau2
                      ,'absolute-tau'        : avg_abs_tau
                      ,'absolute-tau-no-tie' : avg_abs_tau2
                      ,'pair-wise'           : avg_pair }  
         }


############################################################
# rank each cluster

'''
  @Use: Given gold standard and server,
        output algo ranking
        no synonyms considered
'''
def milp_no_syn(gold, app):

  words = join(gold)

  for k in range(0,10):
    shuffle(words)


  pairs      = [u + '-' + v for u in words for v in words if u != v]
  (scores,C) = to_score(pairs,app)

  '''
    initialize problem
  '''  
  prob = LpProblem('-'.join(words), LpMaximize)

  '''
    initialize variables
  '''  
  x = dict()     # real value of each x_i on [0,1]
  d = dict()     # real value of distance between every x_i, x_j, i != j
  w = dict()     # integral value where w_ij => i < j
  s = dict()     # integral value where s_ij => i > j

  for uv in pairs:
    w[uv] = LpVariable('w_' + uv, 0, 1, LpInteger   )
    s[uv] = LpVariable('s_' + uv, 0, 1, LpInteger   )
    d[uv] = LpVariable('d_' + uv, 0, 1, LpContinuous)

  for u in words:
    x[u] = LpVariable('x_' + u, 0, 1, LpContinuous) 


  '''
    objective function
  '''
  objective = [ (w[ij] - s[ij]) * scores[ij] \
                for ij in pairs ]

  prob += lpSum(objective)


  '''
    constraints
  '''
  # d_ij = x_j - x_i
  for ij in pairs:
    [i,j] = ij.split('-')
    prob += x[j] - x[i] == d[ij]

  # d_ij - w_ij * C <= 0
  for ij in pairs:
    prob += d[ij] - w[ij] * C <= 0

  # d_ij + (1 - w_ij) * C > 0
  for ij in pairs:
    prob += d[ij] + (1 - w[ij]) * C >= 0

  # d_ij + s_ij * C >= 0
  for ij in pairs:
    prob += d[ij] + s[ij] * C >= 0

  # d_ij - (1 - sij) * C < 0
  for ij in pairs:
    prob += d[ij] - (1 - s[ij]) * C <= 0


  '''
    solve and interpret data
  '''

  prob.solve()

  algo = prob_to_algo_rank(prob,words)

  if not algo:
    algo = [[w] for w in words]

  return {'gold'           : gold
          ,'algo'          : algo
          ,'tau'           : tau (gold,algo)
          ,'tau-max'       : tau (gold,gold)   # need this since max tau not necessarily 1.0
          ,'tau-notie'     : tau2(gold,algo)
          ,'tau-notie-max' : tau2(gold,gold)
          ,'pairwise'      : pairwise_accuracy(gold,algo)
          ,'raw-score'     : scores
          ,'raw-stat'      : dict()
          }


############################################################
# scores

'''
  @Use: given list of form ['word1-word2', ...]
        output dictonary mapping 'word1-word2' to
        their score, and the normalization constant

  to_score :: [String] -> App -> (Dict String Float, Float)
def to_score(pairs,app):

  one    = app.OneSided
  two    = app.TwoSided
  scores = dict()

  # compute scores
  for uv in pairs:
    [u,v] = uv.split('-')
    s     = markov_score(u,v,one,two)
    scores[uv] = s 

  rescale = min(abs(scores[uv]) for uv in scores \
            if abs(scores[uv]) != 0)

  # normalize scores
  for uv,s in scores.items(): scores[uv] = s/rescale

  C  = sum(abs(scores[uv]) for uv in scores) * 1000

  return (scores, C)
'''

# markov score
def markov_score(ai,ak,one,two):
  p_ik = rank_pairwise(one,two,ai,ak)
  s_ik = p_ik[ak + ' > ' + ai] - p_ik[ai + ' > ' + ak]
  return s_ik












