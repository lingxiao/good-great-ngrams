############################################################
# Module  : Pairwise ranking from derived expression
# Date    : December 21st 2016
# Author  : Xiao Ling
############################################################

from random  import shuffle
from server  import *
from client  import *
from prelude import * 
from app     import * 

############################################################
# Rank from data

'''
  @Use   : infer ranking of all test words from data
  @Input : App
  @Output: A dictionary mapping:
              - 'algo'  to naive ranking
              - 'gold'  to gold ranking
              - 'score' to (word,score) pairs
              - 'tau'   kendall's tau score between gold and naive
'''
def markov_derive(app):
  
  one     = app.OneSided
  two     = app.TwoSided

  ranking = [principle_each(one,two,gold) \
            for _,_,gold in one.test()]

  taus      = [r['tau']             for r in ranking]
  taus2     = [r['tau-notie']       for r in ranking]
  pairs     = [r['pairwise']        for r in ranking]

  avg_tau      = sum(taus)                  / len(taus)
  avg_abs_tau  = sum(abs(t) for t in taus)  / len(taus)
  avg_tau2     = sum(taus2)                 / len(taus2)
  avg_abs_tau2 = sum(abs(t) for t in taus2) / len(taus2)
  avg_pair     = sum(pairs)                 /len(pairs)

  return {'ranking' : ranking
         ,'pattern' : one.pattern()
         ,'average' : {'tau'                 : avg_tau
                      ,'tau-notie'           : avg_tau2
                      ,'absolute-tau'        : avg_abs_tau
                      ,'absolute-tau-no-tie' : avg_abs_tau2
                      ,'pair-wise'           : avg_pair }  
         }


'''
  @Use   : rank words in gold standard list
  @Input : data servers one and two,
           gold standard
  @Output: list of list of words ranked
           weakest to strongest
'''
def principle_each(one,two,gold):

  words   = join(gold)

  for k in range(0,10):
    shuffle(words)

  pairs   = unique_pairs(words)

  ranking = [rank_pairwise(one,two,x,y)   \
             for x,y in pairs]

  raw     = [r['rank'] for r in ranking]

  order = dict()        

  for s,w in raw:
    if s in order:
      order[s] += [w]
    else:
      order[s] = [w]

  # complete the sink in the dictonary
  for w in words:
    if w not in order: order[w] = []



  # algorithm ranking
  algo = [[w] for w in toposort(order)]

  '''
    catch exception in case of cycles
    and just output random permutation
  '''
  if not algo:
    algo = [[w] for w in words]

  # raw score dict
  raw_score = dict()

  for u,v in pairs:
    [d] = [d for d in ranking \
           if d['rank'] == (u,v) \
           or d['rank'] == (v,u)]
    raw_score[u + '-' + v] = d

  return {'gold'          : gold
         ,'algo'          : algo
         ,'tau'           : tau (gold,algo)
         ,'tau-max'       : tau (gold,gold)   # need this since max tau not necessarily 1.0
         ,'tau-notie'     : tau2(gold,algo)
         ,'tau-notie-max' : tau2(gold,gold)
         ,'pairwise'      : pairwise_accuracy(gold,algo)
         ,'raw-score'     : raw_score
         ,'raw-stat'      : dict()
         }


def unique_pairs(words):
  if not words: return []
  else:
    v  = words[0]
    ws = words[1:]
    return [(v,w) for w in ws] + unique_pairs(ws)

# for testing 
def invariant(recon, original):
  bs1 = [o in recon for o in original]
  bs2 = [r in original for r in recon]
  b1  = False not in bs1
  b2  = False not in bs2
  return len(recon) == len(original) and b1 and b2
