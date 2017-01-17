############################################################
# Module  : Naive Learn
# Date    : November 11th, 2016
# Author  : Xiao Ling
############################################################

from random  import shuffle
from server  import *
from client  import *
from prelude import * 
from app     import * 


############################################################
# Learn from data

# @Use   : output list of test words ranked by `naive`
# @Input : None
# @Output: A dictionary mapping:
#             - 'algo'  to naive ranking
#             - 'gold'  to gold ranking
#             - 'score' to (word,score) pairs
#             - 'tau'   kendall's tau score between gold and naive
# naive_learn :: MyApp -> Dict String [[String]]
def markov_absolute(app):

  ranking = [naive_each(app,ws) for (_,_,ws) in app.OneSided.test()]

  taus      = [r['tau']             for r in ranking]
  taus2     = [r['tau-notie']       for r in ranking]
  pairs     = [r['pairwise']        for r in ranking]

  avg_tau      = sum(taus)                  / len(taus)
  avg_abs_tau  = sum(abs(t) for t in taus)  / len(taus)
  avg_tau2     = sum(taus2)                 / len(taus2)
  avg_abs_tau2 = sum(abs(t) for t in taus2) / len(taus2)
  avg_pair     = sum(pairs)                 /len(pairs)

  return {'ranking' : ranking
         ,'pattern' : app.OneSided.pattern()
         ,'average' : {'tau'                 : avg_tau
                      ,'tau-notie'           : avg_tau2
                      ,'absolute-tau'        : avg_abs_tau
                      ,'absolute-tau-no-tie' : avg_abs_tau2
                      ,'pair-wise'           : avg_pair }  
         }


# @Use : Given list of words ranked according to gold standard
#        output navie ranking
# naive :: MyApp -> [[String]] -> [(String,Float)]
def naive_each(app,gold):

  smooth = 1

  words  = join(gold)
  shuffle(words)
  shuffle(words)

  one = app.OneSided
  two = app.TwoSided
  probs  = []
  stat   = dict()

  # naive probs
  for ai in words:
    raw    = one.data(ai)

    strong = sum([n for (_,n) in raw['strong']]) + smooth
    weak   = sum([n for (_,n) in raw['weak'  ]]) + smooth
    freq   = raw['word-freq']

    '''
      measure outdegree/total degree
    '''
    probs.append((ai, strong/weak))
    # probs.append((ai, strong/(strong+weak)))

    # re-save raw data
    stat[ai] = dict()
    stat[ai]['strong']    = strong - smooth
    stat[ai]['weak'  ]    = weak   - smooth
    stat[ai]['word-freq'] = freq

  probs = sorted(probs, key = lambda (ai,n) : n)
  algo  = [[w] for (w,_) in probs]
  probs_dict = dict()
  for word,p in probs:
    probs_dict[word] = p

  return {'gold'           : gold
          ,'algo'          : algo
          ,'tau'           : tau (gold,algo)
          ,'tau-max'       : tau (gold,gold)   # need this since max tau not necessarily 1.0
          ,'tau-notie'     : tau2(gold,algo)
          ,'tau-notie-max' : tau2(gold,gold)
          ,'pairwise'      : pairwise_accuracy(gold,algo)
          , 'raw-score'    : probs_dict
          , 'raw-stat'     : stat}


