

############################################################
# Module  : API to application output and parameters
# Date    : November 11th, 2016
# Author  : Xiao Ling
############################################################

import os
import re
import datetime
from copy    import deepcopy
from prelude import * 
from utils   import *
from server  import * 

############################################################
# 
# Class Interface:
#    - pattern
#    - test
#    - result
# 
#    - write
#    - write_word
#
#    - remove_null_files
# 
# Persistant data stored in objects of this class:
#    - paths to data within the application directory
# 
############################################################

class OutputServer(object):

  # @Input : path/to/good-great
  #          path/to/google-ngram
  # @Output: None
  # init :: OutputServer -> DirectoryPath -> String -> ()
  def __init__(self, in_dir, out_dir, pattern_name, test_set):


    pattern = os.path.join(in_dir, pattern_name + '.txt')
    test    = os.path.join(in_dir, test_set     + '.txt')
    output  = out_dir
    norm    = os.path.join(output, 'total'              )

    [out_pattern, out_word] = make_output_dir(output
                             ,[pattern_name, 'word'])

    self.PATH = {'pattern'      : pattern
                ,'test'         : test
                ,'out-pattern'  : out_pattern
                ,'out-word'     : out_word
                ,'normalization': norm}

    self.normalization = False

  ############################################################
  # Read Output Data

  # @Input : None
  # @Output: strong-weak and weak-strong 
  #          linguistic patterns in this project
  # pattern :: Server -> [String]
  def pattern(self):
    d = dict()
    return read_pattern(self.PATH['pattern'])

  # @Input : None
  # @Output: list where each tuple has:
  #            - antonym pair
  #            - list of list of words where:
  #                 words in the same list are of equal intensity
  #                 words in list_i less intense than words in list_j
  #                 if i < j
  # test :: Server -> [(String,String,[[String]])]
  def test(self):
    return read_test(self.PATH['test'])

  # @Input : word
  # @Output: dictionary mapping
  #             - 'weak'  : dict mapping pattern to count
  #             - 'strong': dict mapping pattern to count
  # results :: String
  #         -> Dict String Float
  def data(self,ai,*args):

    out = deepcopy(self.pattern())

    if not args:
      for key in out:
        Rs       = out[key]
        out[key] = [(R, self.read(ai,R)) for R in Rs]
      out['word-freq'] = self.read(ai)

      return out

    elif len(args) == 1:
      [ak] = args
      for key in out:
        Rs       = out[key]
        out[key] = [(R,self.read(ai,ak,R)) for R in Rs]
      out[ai] = self.read(ai)
      out[ak] = self.read(ak)

      return out

    else:
      raise NameError('Improper input ' + str(args))

  # @Use: read normalization factor 
  def norm(self):

    if not self.normalization:
      strong  = self.pattern()['strong-weak']
      weak    = self.pattern()['weak-strong']
      strongs = [read_total(os.path.join(self.PATH['normalization'], p + '.txt')) \
                 for p in strong]
      weaks   = [read_total(os.path.join(self.PATH['normalization'], p + '.txt')) \
                 for p in weak]
      '''
        catch None type
      '''              
      strongs = [s for s in strongs if s]   
      weaks   = [w for w in weaks   if w]
      
      norm    = {'strong-weak': sum(strongs)
                ,'weak-strong': sum(weaks)}
      self.normalization = norm
      return norm

    else:
      return self.normalization

  # read :: OutputServer -> String -> [String]
  #      -> IO Float
  def read(self,ai,*args):
    p = self.exists(ai,*args)
    print (p)
    if p:
      return read_total(p)
    else: 
      print("missing data for " + ai + ' ' + str(args))
      return 0.0
      # raise NameError("missing data for " + ai + ' ' + str(args))


  # merle

  ############################################################
  # Write Data

  # @Input: word `ai` and `ak`
  #         pattern `R`
  #         Results given in list of (ngram,count) pairs
  # @Ouput: OutputServer. Saves file to system

  # write :: String 
  #       -> [(String,Float)])
  #       -> String
  #       -> [String]
  #       -> IO OutputServer
  def write(self,results, ai, *args):
    if args:
      save(  self.PATH["out-pattern"]
           , to_name(ai,*args)
           , [(args[0],results)])
    else:
      save(self.PATH['out-word'],ai,[('',results)])

  # @Input: word `ai`
  #         Results given in list of (ngram,count) pairs
  # @Ouput: OutputServer. Saves file to system

  # write_strong :: String 
  #              -> [(String,Float)])
  #              -> IO OutputServer
  def write_word(self,ai,results):
    save(self.PATH['out-word'], ai, [("",results)])
    return self

  def write_norm(self,name,results):
  
    out_dir = self.PATH['normalization']
    path    = os.path.join(out_dir,name+".txt")

    if os.path.exists(path):
      os.remove(path)

    '''
      sometimes results have None
    '''
    results = [r for r in results if r]

    total   = sum(n for _,n in results)


    f = open(path,'w')
    f.write(name + "\n")
    f.write(str(datetime.datetime.now())+"\n")
    f.write(demark)
    f.write("cumulative occurrences: " + str(total) + "\n")
    f.write(demark)
  
    for pattern,n in results:
      f.write(pattern + '\t' + str(n) + '\n')
    f.close()    

    return self



  ############################################################
  # Ping data 

  # @Use   : server.exists('good',['great','* but not *'])
  # @Input : word
  # @Optional input: word, pattern
  # @Output: Boolean YES if file exists
  # exists :: App -> String -> Optional String -> Bool
  def exists(self,ai,*args):

    paths = self.PATH

    if args:
      path = os.path.join(paths['out-pattern'], to_name(ai,*args) + '.txt')

      if os.path.isfile(path): return path
      else                   : return False

    else:
      path1 = os.path.join(paths['out-word']     , to_name(ai,*args) + '.txt')
      path2 = os.path.join(paths['normalization'], ai                + '.txt')

      if os.path.isfile(path1)  : return path1
      elif os.path.isfile(path2): return path2
      else                      : return False

  ############################################################
  # Maintain directory

  '''
    @Use: for what ever reason sometimes files are saved
          with no content, remove these files          
  '''
  def remove_null_files():
    path   = self.PATH['out-pattern']
    files  = os.listdir(path)
    files1 = [f.replace('.txt','') + '-1' + '.txt' for f in files] 
    paths  = [os.path.join(path,f) for f in files]

    log('removing null files')

    for p in paths:
      f = open(p,'r').read()
      if not f:
        os.remove(p)
        print ('removing ' + p)


# naming convention
# to_name :: String -> String -> String -> String
def to_name(ai,*args):
  if not args:
    return ai 
  elif len(args) == 1:
    [R] = args
    return ai + "-" + R
  elif len(args) == 2:
    [ak,R] = args
    return ai + '-' + str(ak) + '-' + str(R)
  else:
    return ''


demark = "------------------------------------------------\n"





