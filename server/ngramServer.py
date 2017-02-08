############################################################
# Module  : API to application Input
# Date    : November 11th, 2016
# Author  : Xiao Ling
############################################################

import os
import re
import datetime
from prelude import * 

############################################################
# 
# Class Interface:
#   - filter
#   - b_filter
#   - read
# 
# Persistent data:
#   - directory path
# 
############################################################

class NgramServer(object):

  # @Input : path/to/good-great
  #          path/to/google-ngram
  # @Output: None
  # init :: InputServer -> DirectoryPath -> DirectoryPath -> _|_
  def __init__(self, ngram_dir, hack):
    self.PATH  = config(ngram_dir, hack)
    self.store = []

############################################################
  # Read and filter ngram data

  # @Input : Index indicating which n-gram directory to 
  #          filter over:
  #             - -1: grepped total-patterns
  #             - 0:  grepped ngrams
  #             - 1:  1-gram
  #             - 2:  2-gram
  #             - 3:  3-gram
  #             - 4:  4-gram
  #             - 5:  5-gram
  # 
  #          Predicate taking each line of ngram stirpped of
  #          counts as parameter
  # @Output: Generator yielding all ngrams in corpus
  #          that matches pattern

  # filter_ngram :: Server
  #              -> Int
  #              -> (Text -> Bool)
  #              -> Gen (String,Float)
  def filter(self,n,pred):
    # todo: get rid of this dangerous persistence
    store = self.stock_store(n)
    return [split_ngram(xs) for xs in store if pred(xs)]

  # @Input : Index indicating which n-gram directory to 
  #          filter over:
  #             - 0:  grepped ngrams
  #             - 1:  1-gram
  #             - 2:  2-gram
  #             - 3:  3-gram
  #             - 4:  4-gram
  #             - 5:  5-gram
  # 
  #          List of tuples:
  #            - (predicate, keyword)
  # @Output: list of all ngrams in corpus
  #          that matches predicate 

  # batch_filter :: NgramServer -> Int 
  #              -> [(String -> Bool, String, [String])]
  #              -> [([String], String, String)]
  def batch_filter(self,n,preds):
    store  = self.stock_store(n)
    stores = [go_filter([line for line in store if 
              word_in_line(line,ws)],p,R,ws)    \
              for (p,R,ws) in preds]

    return stores

  # @Input  : Index indicating which ngram directory to read
  # @Output : Generator outputting all grepped ngrams 
  #           in directory `corpus`
  # read_ngram :: Server -> Int -> Gen String
  def read(self,n):

    for line in fetch_ngrams(n,self.PATH):
      yield split_ngram(line)

  def stock_store(self,n):
    if not self.store: 
      self.store = list(set(fetch_ngrams(n,self.PATH)))
    return self.store

  # reset store
  def reset_store(self):
    self.store = []

############################################################
# PRIVATE FUNCTIONS
############################################################

############################################################
# filter files

# go_filter :: [String] 
#           -> (String -> Bool) 
#           -> String 
#           -> String 
#           -> [([String], String, String)]
def go_filter(grams,pred,pattern,words):
  print ("=== collecting data for " + pattern + " at word: " + ' '.join(words))
  results = [split_ngram(xs) for xs in grams if pred(xs)]
  return (results, pattern, words)


def word_in_line(line,words):
  matches = [w for w in words if w in line]
  return len(matches) == len(words)


# @Input  : ngram of form "xxx ... xxx ###"
# @Output : a tuple ("xxx ... xxx ###", ###)
# split_ngram :: String -> (String,Float)
def split_ngram(xs):
  ts = xs.split("\t")
  if len(ts) == 2:
    return (ts[0],float(ts[1]))

############################################################
# read file 

# fetch_ngrams :: Int -> PATH -> IO (Gen String)
def fetch_ngrams(n, PATH):

    file_paths = pick_corpus(PATH,n)

    for f in file_paths:
      raw   = open(f,'r')
      raw   = raw.read()
      lines = raw.split('\n')
      for line in lines:
        yield line

# pick_corpus :: Dict String DirectoryPath 
#             -> Int 
#             -> [FilePath]
def pick_corpus(PATH,n):
  if n == 0:
    corpus = PATH['grep']
  elif n == 1:
    corpus = PATH['1gms']
  elif n == 2:
    corpus = PATH['2gms']
  elif n == 3:
    corpus = PATH['3gms']
  elif n == 4:
    corpus = PATH['4gms']
  elif n == 5:
    corpus = PATH['5gms']

  return [os.path.join(corpus,f) for f in os.listdir(corpus)]


############################################################
# Init

# @USE:  path/to/ngram
# Output CONFIG mapping name to directories if all 
# directories valid. else throw error

# config :: DirectoryPath
#        -> Eff [IO, Error String] (Dict String DirectoryPath)
def config(ngram_dir, hack):
  if not os.path.isdir(ngram_dir):
    raise NameError("Invalid Directory: " + ngram_dir)
  else:

    normalized = os.path.join(ngram_dir, 'normalized')

    p_1gm = os.path.join(normalized,"1gms")
    p_2gm = os.path.join(normalized,"2gms")
    p_3gm = os.path.join(normalized,"3gms")
    p_4gm = os.path.join(normalized,"4gms")
    p_5gm = os.path.join(normalized,"5gms")

    '''
    # hack: for twosided pattern we simply
            crawl onesided patterns we previously collected

    '''
    # grep  = '/Users/lingxiao/Documents/research/code/good-great-ngrams/outputs-2/one-sided-patterns'
    grep  = os.path.join(ngram_dir ,"grepped/grepped-data")

    raise_errors([p_1gm, grep])

    return { "grep"  : grep
           , "1gms"  : p_1gm
           , "2gms"  : p_2gm
           , "3gms"  : p_3gm
           , "4gms"  : p_4gm
           , "5gms"  : p_5gm}

# raise_errors :: [String] -> Eff [IO, Error String) ()
def raise_errors(paths):
  for p in paths:
    if not os.path.isdir(p) and not os.path.isfile(p):
      raise NameError("Path invalid: " + p)


