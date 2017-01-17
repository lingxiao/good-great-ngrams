############################################################
# Module  : Filter veronica's stuff for adjectives
# Date    : November 19th
# Author  : Xiao Ling
############################################################

from nltk import * 


path = '/Users/lingxiao/Desktop/all_adjectives.txt'
out  = '/Users/lingxiao/Desktop/adjectives.txt'

f = open(path,'r')
xs = f.read()
xs = xs.split('\n')

tagged = pos_tag(xs)
jjs    = [a for (a,t) in tagged if t == 'JJ'  \
                                or t == 'JJR' \
                                or t == 'JJS' ]

h = open(out,'w')
for a in jjs:
	h.write(a + '\n')
h.close()

