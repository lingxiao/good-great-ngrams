############################################################
# Module  : Scores
# Date    : November 8th
# Author  : Xiao Ling
############################################################

from prelude import * 

# @Input : Dictionary mapping linguistic pattern type
#          to total occurences of patterns in type in corpus
#          Dictionary mapping linguistic pattern types 
#          (1) weak and (2) strong to:
#              for each i and k:
#                   - "ai-ak": total occurences of ai-ak
#                  in corpus in presence of weak patterns
#          and (3) word to their occurences
# @Output: Dictinoary mapping for every i and k:
#             - word 'ai-ak' to their normalized score(ai,ak)
#               where:
# 
#                          (W1 - S1) - (W2 - S2)
#       score(ai,ak) =  --------------------------
#                           cnt(ai) * cnt(ak)
# 
#          where W1 = 1/P1 * w1 = 1/P1 * sum_{p in P_ws} cnt(p(ai,ak))
#          where W2 = 1/P1 * w2 = 1/P1 * sum_{p in P_ws} cnt(p(ak,ai))
#          where S1 = 1/P2 * s1 = 1/P2 * sum_{p in P_sw} cnt(p(ai,ak))
#          where W2 = 1/P2 * s2 = 1/P2 * sum_{p in P_sw} cnt(p(ak,ai))

# score_all :: Dict String Float 
#       -> Dict String (Dict String Float)
#       -> Dict String Float
def score_all(norm,data):
	d    = dict()
	ws   = get_words(data)
	pws  = [(ai,ak) for ai in ws for ak in ws if ai != ak]
	minv = 1e10

	for (ai,ak) in pws:
		n = score(norm,data,ai,ak)
		if n and abs(n) < minv: minv = abs(n)
		d[ai + '-' + ak] = n

	for aik in d:
		d[aik] = d[aik]/minv

	return d


############################################################
# Helper functions


def get_words(data):
	return [w for w,_ in data['word'].iteritems()]


# score :: Dict String Float 
#       -> Dict String (Dict String Float)
#       -> String
#       -> String
#       -> Float
def score(norm, data, ai, ak):
	strong = data['strong-weak']
	weak   = data['weak-strong']
	word   = data['word'       ]
	P1     = norm['weak-strong']
	P2     = norm['strong-weak']

	top    = (W1(P1,weak,ai,ak) - S1(P2,strong,ai,ak)) \
	       - (W2(P1,weak,ai,ak) - S2(P2,strong,ai,ak))

	bot    = word[ai] * word[ak]

	return top/bot



# @Input : Normalization constant
#          word-value dctionary mapping for each i and k:
#           - "ai-ak": total occurences of ai-ak
#                      in corpus in presence of weak patterns
#          words `ai` and `ak`
# @Output: W1 score as defined in paper:
#          W1 = 1/P1 * w1 = 1/P1 * sum_{p in P_ws} cnt(p(ai,ak))

# W1 : Float 
#      -> Dict String Float 
#      -> String
#      -> String
#      -> Float
def W1(P1, weak, ai, ak):
	name = ai + "-" + ak
	return weak[name]/P1

def W2(P1, weak, ai, ak):
	name = ak + "-" + ai
	return weak[name]/P1

def S1(P2, strong, ai, ak):
	name = ai + "-" + ak
	return strong[name]/P2

def S2(P2, strong, ai, ak):
	name = ak + "-" + ai
	return strong[name]/P2























