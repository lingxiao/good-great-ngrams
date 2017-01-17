############################################################
# Module  : Application IO
# Date    : November 19th, 2016
# Author  : Xiao Ling
############################################################

import os
import re
import datetime
from server  import *
from client  import *
from prelude import * 

############################################################
# query server for a regex

# Note to self: this is where we differentiate
# between collecting from preprocessed 4 and 5 grams
# versus preprocessed and grepped google ngrams
# query_server :: InputServer -> Regex -> [(String,Int)]
def query_server(ngram_server,regex):
  pred = predicate(regex)
  out  = ngram_server.filter(0,pred)
  # out  = list(ngram_server.filter(4,pred)) \
       # + list(ngram_server.filter(5,pred)) 
  return out

# predicate :: RegularExpression -> String -> Bool
def predicate(regex):
    def go(text):
      t = text.lower().strip()
      return regex.match(t) != None
    return go

############################################################
# collect data for an individual regex

# @ Input : `diff` flag, if True then
#           overwrite existsing data
#           if False then do not overwrite data
#           server for application data
#           server for ngram data
# @ Ouput : results

# collect_word :: Bool 
#              -> InputServer 
#              -> OutputServer
#              -> IO [(String,Int)]
def collect_word(diff, ngram_server,app_server,ai):
  if diff and app_server.exists(ai):
    log("Data for " + ai + " already exists")
    return []
  else:
    log ("collecting data for word: " + ai)
    r   = re.compile(ai + "[\s]+")
    out = list(ngram_server.filter(1,predicate(r)))
    app_server.write_word(ai,out)
    return out 

############################################################
# Utils

# log :: String -> IO ()
def log(xs):
  header = "======================  "
  print (header + xs + "\n")

