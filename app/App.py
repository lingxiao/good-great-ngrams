############################################################
# Module  : Paper Application Interface
# Date    : November 11th, 2016
# Author  : Xiao Ling
############################################################

import os
import re
import datetime
from random  import shuffle
from server  import *
from client  import *
from prelude import * 
from app     import * 

############################################################
# 
# Class Interface:
#   - run
#   - refresh
#   - learn
#   - distill
#   - to_one_sided
#   - refresh_word
# 
# Persistant data stored in objects of this class:
#    - paths to ngram data and 
#      data within the application directory
# 
############################################################

class App(object):

  # @Input : path/to/good-great
  #          path/to/google-ngram
  #          path/to/output-directory
  #          path/to/one-sided-pattern.txt
  #          path/to/two-sided-pattern.txt
  # @Output: None
  # init :: App -> DirectoryPath -> DirectoryPath -> _|_
  def __init__(self \
              ,root \
              ,ngram \
              ,out_dir \
              ,one_sided_patterns \
              ,two_sided_patterns
              ,test_set):

    in_dir          = os.path.join(root,'inputs')
    out_dir         = os.path.join(root, out_dir )

    self.root       = root
    self.output_dir = out_dir
    self.input_dir  = in_dir
    self.OneSided   = OutputServer(in_dir, out_dir, one_sided_patterns, test_set)
    self.TwoSided   = OutputServer(in_dir, out_dir, two_sided_patterns, test_set)
    self.NGRAM      = NgramServer (ngram, False)

  ############################################################
  # Collect data

  # @Use   : fetches test set and collect all data
  # @Input : None
  # @Ouput : App
  # run :: App -> IO App
  def run(self):
    log("Re-Running Entire Application")
    run_all(False, 2, self.OneSided, self.TwoSided, self.NGRAM)
    run_all(False, 1, self.OneSided, self.TwoSided, self.NGRAM)
    return self

  # @Use: refresh application and run any new
  #       vocabulary and relations added since last run
  #       also runs normalization if it does not exist
  # @Input:  number 1 or 2, for refresh onesided or two sided
  # @Output: App
  # refresh :: App -> Int -> IO App
  def refresh(self, n):
    log("Refreshing Application")
    run_all(True, n, self.OneSided, self.TwoSided, self.NGRAM)
    log ("All Application Data Up To Date")
    return self

  def refresh_word(self):
    collect_word(True, self.NGRAM,self.OneSided)

  ############################################################
  # write results

  # @Input: name of file
  #         A dictionary mapping:
  #             - 'algo'  to naive ranking
  #             - 'gold'  to gold ranking
  #             - 'score' to (word,score) pairs
  #             - 'tau'   kendall's tau score between gold and naive
  # @Output: None
  # save :: MyApp -> String -> Result -> IO ()
  def save(self,name,results):
    ranking  = results['ranking']
    average  = results['average']
    patterns = results['pattern']

    avg_taus          = average['tau']
    avg_abs_taus      = average['absolute-tau']
    avg_pairwise      = average['pair-wise']
    avg_tau_notie     = average['tau-notie']
    avg_abs_tau_notie = average['absolute-tau-no-tie']

    path = os.path.join(self.root, name + '.txt')
    f    = open(path,'w')
    f.write(name + '\n')
    f.write(str(datetime.datetime.now()) + '\n')

    f.write(demark)
    f.write('average tau:  '             + str(round(avg_taus            ,2)) + '\n')
    f.write('average |tau|: '            + str(round(avg_abs_taus        ,2)) + '\n')
    f.write('average tau  no tie  '      + str(round(avg_tau_notie       ,2)) + '\n')
    f.write('average |tau| no tie  '     + str(round(avg_abs_tau_notie   ,2)) + '\n')
    f.write('average pairwise accuracy: '+ str(round(avg_pairwise*100)) + '%\n')
    f.write(demark)

    for rank in ranking:
      
      f.write('=== tau:\n'               + str(rank['tau'])       + '\n\n')
      f.write('=== pairwise accuracy:\n' + str(rank['pairwise'])  + '\n\n')

      f.write('=== gold: \n')      
      for w in rank['gold']:
        f.write(str(w) + '\n')
      f.write('\n')

      f.write('=== algo: \n')      
      for w in rank['algo']:
        f.write(str(w) + '\n')
      f.write('\n')

      f.write('=== raw score: \n')      
      for w in rank['raw-score']:
        f.write(str(w) + ': ' 
                       + str(rank['raw-score'][w]) + '\n')
      f.write('\n')

      stat = rank['raw-stat']

      f.write('=== raw counts: \n')      
      for word in stat:
        f.write(word + '\n')
        vals = stat[word]
        for val in vals:
          f.write('\t' + val + ': ' + str(vals[val])+ '\n')


      f.write(demark)

    [pkey1, pkey2] = [key for key in patterns]
        
    f.write('\n')
    f.write(demark)
    f.write('Patterns Used: \n')
    f.write(demark)

    f.write('=== strong\n')
    f.write('\n')
    for p in patterns[pkey1]:
      f.write(p + '\n')

    f.write('\n')
    f.write('=== weak\n')
    f.write('\n')

    for p in patterns[pkey2]:
      f.write(p + '\n')

    f.write('\n=== END')


    f.close()

  # @Use: find two-sided-pattern.txt in inputs directory
  #       and convert them to one-sided-patterns
  #       save result to good-great/one-sided-patterns.txt
  def to_one_sided(self):

    # path = os.path.join(self.root, 'auto-generated-one-sided-patterns.txt')
    path = os.path.join(self.root + '/inputs', 'one-sided-patterns.txt')

    # two sided patterns
    pattern     = self.TwoSided.pattern()
    strong_weak = pattern['strong-weak']
    weak_strong = pattern['weak-strong']

    # one sided patterns
    strong = []
    weak   = []

    for p in strong_weak:
      strong.append(fill_snd(p))
      weak.append  (fill_fst(p))

    for p in weak_strong:
      strong.append(fill_fst(p))
      weak.append  (fill_snd(p))

    h = open(path,'w')

    h.write('=== strong\n\n')
    [h.write(p + '\n\n') for p in strong]

    h.write('=== weak\n\n')
    [h.write(p + '\n\n') for p in weak]

    h.write('=== END')

    h.close()

  # @Input: None
  # @Ouput: None. Write to disk
  #         raw counts of all words over all patterns
  def distill(self):
    name1 = 'one-sided-patterns-data'
    name2 = 'two-sided-pattern-data'
    distill_ones (self.root,name1,self.OneSided)
    distill_pairs(self.root,name2,self.TwoSided)

# demarcation in file
demark = "------------------------------------------------\n"

############################################################
# PRIVATE FUNCTIONS
############################################################

############################################################
# collect data

# @ Input : `refresh` flag, if True then
#           overwrite existsing data
#           if False then do not overwrite data
#           `n` denoting one-sided or two-sided patterns
#           server for application data
#           server for ngram data
#           list of words [ai,ak,...]
#           to collect data over
# 
# @ Ouput : None
# run_all :: InputServer
#      ls      -> OutputServer
#            -> IO ()
def run_all(refresh, n, onesided, twosided, ngram):
  
  test = [ws for (_,_,ws) in onesided.test()]

  if n == 1:
    collect_one_sided    (refresh,ngram,onesided,join(join(test)))
  elif n == 2:    
    collect_two_sided    (refresh,ngram,twosided,test)
    collect_normalization(refresh,ngram,twosided)
    collect_word         (refresh,ngram,onesided)
  else:
    raise NameError('Improper input ' + str(n))



# TODO: this is not the fn that is run for most of the project
#       need to catch a bug in here
def collect_word(refresh,ngram,one):
  words   = set(join(join(xs for _,_,xs in one.test())))
  preds   = [('',ai) for ai in words]
  queries = []

  for (R,ai) in preds:
    if refresh and one.exists(ai):
      pass
      log ("Data for " 
          + ai  + " " 
          + "already exists")
    else:
      pred = predicate(re.compile(parse_re(ai,[])))
      queries.append((pred,'',[ai]))

    if queries:
      for (pred,r,[ai]) in queries:
        result = ngram.filter(1,pred)
        one.write_word(ai,result)
        log('collecting data for ' + ai + '\n')

        
def collect_normalization(refresh,ngram,twosided):

  patts    = twosided.pattern()
  patterns = join([patts[key] for key in patts])
  queries  = []

  for R in patterns:
    if twosided.exists(R) and refresh:
      log('pattern ' + R + ' already exists')
    else:
      pred = predicate(re.compile(parse_re(R,[])))
      queries.append( (pred, R, [key_word(R)])  )

  batchs = chunks(queries,5)
  incr   = 1

  for batch in batchs:
    log('collecting data for batch ' + str(incr) + '\n')

    results = ngram.batch_filter(0,batch)
    [twosided.write_norm(R,rs) for (rs,R,_) in results]

    log('Saving results ...')
    incr += 1

  log("Finished!")

def collect_one_sided(refresh,ngram,onesided,words):

  d         = onesided.pattern()
  patterns  = join([d[key] for key in d])
  all_preds = [(R,ai) for R in patterns for ai in words]
  queries   = []

  for (R,ai) in all_preds:
    if refresh and onesided.exists(ai,R):
      pass
      log ("Data for " 
          + ai  + " " 
          + R   + " "
          + "already exists")
    else:
      pred = predicate(re.compile(parse_re(R,[ai])))
      queries.append((pred,R,[ai]))

  if queries:
    current = chunks(queries,30)
    incr    = 1
    for query in current:

      log ('Collecting data for batch ' + str(incr) + '\n')

      results = ngram.batch_filter(0, query)
      [onesided.write(result,ai,R) for (result,R,[ai]) in results]

      log('Saving results ...')
      incr += 1

def collect_two_sided(refresh, ngram, twosided, words):

  pwords    = fmap(lambda xs: [(u,v) for u in join(xs) for v in join(xs) if u != v], words)
  d         = twosided.pattern()
  patterns  = join([d[key] for key in d])
  all_preds = join(fmap (lambda xs : [(R,ai,ak) for R in patterns for (ai,ak) in xs]
                   , pwords))

  log ('building queries ...')

  if refresh:
    queries = [to_query(R,ai,ak) for (R,ai,ak) in all_preds if \
               not_exist(twosided,R,ai,ak)]
  else:
    queries = [to_query(R,ai,ak) for (R,ai,ak) in all_preds]

  if queries: 
    log('querying database ...')

    current = chunks(queries,20)
    incr    = 1

    for query in current:
      log('Collecting data for batch ' + str(incr) + '\n')

      results = ngram.batch_filter(0,query)
      [twosided.write(result,ws[0],ws[1],R) for (result,R,ws) in results]
      
      log('Saving results ...')      
      incr += 1

def not_exist(twosided, R,ai,ak):
  if twosided.exists(ai,ak,R):
      log ("data for " + ai + " " + ak + " " + R + " already exists")
      return False
  else:
    return True

def to_query(R,ai,ak):
  r = re.compile(parse_re(R,[ai,ak]))
  return ( predicate(r), R, [ai,ak])

def key_word(pattern):
  words = pattern.split(' ')
  for word in words:
    if word != '*' and word[0] != '(' and word != '<*>':
      return word
  return ' '


############################################################
# Distill

def distill_ones(root, name, server):

  words = [(u,v,join(ws)) for (u,v,ws) in server.test()]
  out   = []

  for (u,v,alist) in words:
    ret = [(ai,server.data(ai)) for ai in alist]
    out.append((u,v,ret))

  path  = os.path.join(root, name + '.txt')
  f     = open(path,'w')

  f.write(demark)
  f.write(demark)
  f.write(name + '\n')
  f.write(str(datetime.datetime.now()) + '\n')
  f.write(demark)
  f.write(demark + '\n\n')

  for (u,v,ret) in out:
    f.write('=== ' + u + ' ' + v + '\n\n')
    for (ai,results) in ret:
      f.write('=== word: ' + ai + '\n\n')
      for key in results:
        if key == 'word-freq':
          pass
        else:
          patterns = results[key]
          f.write('== ' + key + '\n\n')
          for (p,n) in patterns:
            f.write(p + '\t' + str(n) + '\n')
        f.write('\n')
    f.write(demark)
    f.write(demark)

  f.close()

def distill_pairs(root, name, server):

  # compile a list of all words and counts
  pairs = [(u,v,to_pair(ws)) for (u,v,ws) in server.test()]

  out = []
  for (u,v,plist) in pairs:
    ret = [(ai,ak,server.data(ai,ak)) for (ai,ak) in plist]
    out.append((u,v,ret))


  path = os.path.join(root, name + '.txt')
  f    = open(path,'w')
  
  f.write(demark)
  f.write(demark)
  f.write(name + '\n')
  f.write(str(datetime.datetime.now()) + '\n')
  f.write(demark)
  f.write(demark + '\n\n')

  for (u,v,ret) in out:
    f.write('=== ' + u + ' ' + v + '\n\n')
    for (ai,ak,results) in ret:
      f.write('=== word pair: ' + ai + ', ' + ak + '\n\n')
      for key in results:
        if key == 'word-freq':
          pass
        else:
          patterns = results[key]
          f.write('== ' + key + '\n\n')
          for (p,n) in patterns:
            f.write(p + '\t' + str(n) + '\n')
        f.write('\n')
    f.write(demark)
    f.write(demark)

  f.close()

def to_pair(ws):
  ws = join(ws)
  return [(ai,ak) for ai in ws for ak in ws if ai != ak]


############################################################
# converting twosided patterns to onesided 
'''
def fill_fst(p):
  return ' '.join(fill(p.split(' ')))

def fill_snd(p):
  p = p.split(' ')
  p.reverse()
  ws = fill(p)
  ws.reverse()
  return ' '.join(ws)

def fill(ws):
  i  = ws.index('*')
  ws[i] = '<*>'
  return ws
'''