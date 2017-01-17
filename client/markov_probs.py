############################################################
# Module  : Pairwise ranking from derived expression
# Date    : December 21st 2016
# Author  : Xiao Ling
############################################################

import random
from random  import shuffle
from server  import *
from client  import *
from prelude import * 
from app     import * 

############################################################
# Infer Each Pair


'''
  @Use   : rank words x and y 
  @Input : data servers one and two,
           words x and y
  @Output: tuple (a,b) read as: a > b
'''
def rank_pairwise(one,two,u,v):

  d = rank_pairwise_two_sided(two,u,v)
  if d: return d
  else: return rank_pairwise_one_sided(one,two,u,v)


'''
  Approximate xPy using one-sided patterns
'''
def rank_pairwise_one_sided(one,two,u,v):

    pstrong  = two.pattern()['strong-weak']
    pweak    = two.pattern()['weak-strong']

    star_strong_star = two.norm()['strong-weak']

    star_weak_star   = two.norm()['weak-strong']

    # cnt (x Strong *)
    u_strong_star = w_strong_star(one,two,u)

    # cnt (x Weak *)
    u_weak_star = w_weak_star(one,two,u)

    # cnt (y Strong *)
    v_strong_star = w_strong_star(one,two,v)

    # cnt (y Weak *)
    v_weak_star = w_weak_star(one,two,v)

    # cnt (* Strong y)
    star_strong_v = star_strong_w(one,two,v)

    # cnt (* Strong x)
    star_strong_u = star_strong_w(one,two,u)

    # cnt (* Weak x)
    star_weak_u = star_weak_w(one,two,u)

    # cnt (* Weak y)
    star_weak_v = star_weak_w(one,two,v)


    # Pr(x Strong y)
    u_strong_v = (u_strong_star * star_strong_v) \
                 / star_strong_star

    # Pr(y Weak x)
    v_weak_u   = (v_weak_star   * star_weak_u  ) \
                 / star_weak_star

    # Pr (y Strong x)
    v_strong_u = (v_strong_star * star_strong_u) \
                 / star_strong_star

    # Pr(x Weak y)
    u_weak_v   = (u_weak_star   * star_weak_v ) \
                 / star_weak_star

    # Pr(x > y  or y < x)
    Pr_u_stronger_v = u_strong_v + v_weak_u

    # Pr(y > x or x < y)
    Pr_v_stronger_u = v_strong_u + u_weak_v


    '''
      derived measure rank
    '''

    if Pr_u_stronger_v >= Pr_v_stronger_u:
      r = (u,v)
    else: 
      r = (v,u)

    # Pr[x > y]
    p = u + ' > ' + v
    q = v + ' > ' + u

    print ('=== :' + p + ' ' + str(Pr_u_stronger_v))
    print ('=== :' + q + ' ' + str(Pr_v_stronger_u))


    return {'rank'         : r
           ,p              : Pr_u_stronger_v
           ,q              : Pr_v_stronger_u}

'''
  Determine xPy using two-sided patterns
'''
def rank_pairwise_two_sided(two,u,v):

  eps = 1.0

  u_strong_weak_v = sum(n for _, n in two.data(u,v)['strong-weak'])
  v_weak_strong_u = sum(n for _, n in two.data(v,u)['weak-strong'])

  u_weak_strong_v = sum(n for _, n in two.data(u,v)['weak-strong'])
  v_strong_weak_u = sum(n for _, n in two.data(v,u)['strong-weak'])

  if not u_strong_weak_v  and not v_weak_strong_u \
  and not u_weak_strong_v and not v_strong_weak_u:

    print ('=== no data')

    return False

  else:
    u_strong = u_strong_weak_v + eps + v_weak_strong_u + eps
    v_strong = u_weak_strong_v + eps + v_strong_weak_u + eps

    print (u + ' u strong', u_strong)
    print (v + ' v strong', v_strong)

    Pr_u_stronger_v = (u_strong + eps)/(u_strong + v_strong)
    Pr_v_stronger_u = 1.0 - Pr_u_stronger_v

    if Pr_u_stronger_v >= Pr_v_stronger_u:
      r = (u,v)
    else: 
      r = (v,u)

    # Pr[x > y]
    p = u + ' > ' + v
    q = v + ' > ' + u

    print ('=== :' + p + ' ' + str(Pr_u_stronger_v))
    print ('=== :' + q + ' ' + str(Pr_v_stronger_u))

  return {'rank'         : r
         ,p              : Pr_u_stronger_v
         ,q              : Pr_v_stronger_u}


############################################################
# Pairwise comparisons

# given a strong-weak twosided pattern, pick out
# the corresponding strong-weak one-sided pattern in strong
def w_strong_star(one,two,x):
  pstrong     = two.pattern()['strong-weak']
  pweak       = two.pattern()['weak-strong']
  strong_data = one.data(x)['strong']
  weak_data   = one.data(x)['weak'  ]

  pstrong1 = [fill_snd(p) for p in pstrong]
  pairs    = [(q,pn) for q in pstrong1 for pn in strong_data]
  data     = [(p,n) for (q,(p,n)) in pairs if p == q]
  return sum(n for p,n in data)

def star_strong_w(one,two,x):
  pstrong     = two.pattern()['strong-weak']
  pweak       = two.pattern()['weak-strong']
  strong_data = one.data(x)['strong']
  weak_data   = one.data(x)['weak'  ]

  pstrong2 = [fill_fst(p) for p in pstrong]
  pairs    = [(q,pn) for q in pstrong2 for pn in weak_data]
  data     = [(p,n) for (q,(p,n)) in pairs if p == q]
  return sum(n for p,n in data)

def w_weak_star(one,two,x):
  pstrong     = two.pattern()['strong-weak']
  pweak       = two.pattern()['weak-strong']
  strong_data = one.data(x)['strong']
  weak_data   = one.data(x)['weak'  ]

  pweak1   = [fill_snd(p) for p in pweak]
  pairs    = [(q,pn) for q in pweak1 for pn in weak_data]
  data     = [(p,n) for (q,(p,n)) in pairs if p == q]
  return sum(n for p,n in data)

def star_weak_w(one,two,x):
  pstrong     = two.pattern()['strong-weak']
  pweak       = two.pattern()['weak-strong']
  strong_data = one.data(x)['strong']
  weak_data   = one.data(x)['weak'  ]

  pweak2   = [fill_fst(p) for p in pweak]
  pairs    = [(q,pn) for q in pweak2 for pn in strong_data]
  data     = [(p,n) for (q,(p,n)) in pairs if p == q]
  return sum(n for p,n in data)

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
