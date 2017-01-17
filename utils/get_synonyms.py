############################################################
# Module  : get all synonyms
# Date    : November 24th
# Author  : Xiao Ling
############################################################

from nltk.corpus import wordnet as wn
import os

from prelude import * 
from utils   import *
from server  import * 
from client  import * 
from app     import * 

############################################################
# Initialize application 
############################################################

root   = "/Users/lingxiao/Documents/research/code/good-great"
output = OutputServer(root)

############################################################
# Initialize application 
############################################################

words = join(join([ws for (_,_,ws) in output.test()]))

synonyms = []

for word in words:
	syns = wn.synsets(word,pos = wn.ADJ    ) \
	     + wn.synsets(word,pos = wn.ADJ_SAT)
	syns = [w.name().split('.')[0] for w in syns]
	synonyms += syns

synonyms = set(synonyms)


out = os.path.join(root,'synonyms.txt')

f = open(out,'w')


f.write('=== synonyms, synonyms **\n')

for w in synonyms:
	f.write(w + '\n')

f.write('=== END')
f.close()







