############################################################
# Module  : Common IO functions for all servers
# Date    : November 19th, 2016
# Author  : Xiao Ling
############################################################

import os
import re
import datetime
from prelude import * 
from utils   import *
from server import * 

############################################################
# Initialization

def make_output_dir(output, dirs):

  if not os.path.isdir(output):
    os.makedirs(output)

  sub_dirs = [os.path.join(output,d) for d in dirs]

  for d in sub_dirs:
    if not os.path.isdir(d):
      os.makedirs(d)

  return sub_dirs


# raise_errors :: [String] -> Eff [IO, Error String) ()
def raise_errors(paths):
  for p in paths:
    if not os.path.isdir(p) and not os.path.isfile(p):
      raise NameError("Path invalid: " + p)

############################################################
# Saving results

# @Use  : save `results` to file named `name` in 
#         output directory `out_dir`
#         if file already exists, overwrite it 
# @Input: Directory path
#         words `ai` and `ak`
#         parsing results
# @Output: None. write to disk
# save :: DirectoryPath 
#         -> String
#         -> [(String, [(String,Float)])] 
#         -> IO ()
def save(out_dir,name,results):


  # sometimes results list have None as item
  results = [r for r in results if r]

  path    = os.path.join(out_dir,name+".txt")

  if os.path.exists(path):
    os.remove(path)

  totals  = [(p,sum(n for _,n in out)) for p,out in results]
  total   = sum([n for (_,n) in totals])

  f = open(path,'w')
  f.write(name + "\n")
  f.write(str(datetime.datetime.now())+"\n")
  f.write(demark)
  f.write("cumulative occurrences: " + str(total) + "\n")
  f.write(demark)
  for (pattern,result) in results:
      f.write(pattern + "\n")
      n = [n for (t,n) in totals if t == pattern]
      f.write("pattern occurrences: " + str(n[0]) + "\n")
      for (xs,n) in result: f.write(xs + "\t" + str(n) + "\n")
      f.write(demark)
  f.close()    


# demarcation in file
demark = "------------------------------------------------\n"


############################################################
# Read Specific Assets


# read_pattern :: FilePath -> Dict String [String]
def read_pattern(path):

  h    = [x.strip() for x in open(path,'r').read().split('===') if x.strip()]
  xxs  = [x.split('\n') for x in h]

  d = dict()
  for xs in xxs:
   if xs[0] != 'END':
    d[xs[0]] = [x.strip() for x in xs[1:] if x]

  return d


# read_test :: FilePath -> IO [String]
def read_test(path):
  raw = [r for r in open(path,'r').read().split('=== ') if r]
  raw = [r.split('\n') for r in raw]
  raw = [r for r in raw if r][0:-1]

  test = []

  for xs in raw:
    u,v = xs[0].split(', ')
    ys  = [x.split(', ') for x in xs[1:] if x]
    test.append((u,v,ys))

  return test

# get_pairs :: String -> [(String,String)]
def get_pairs(xs):
  ys = xs.split("\n")
  ps = [to_pair(p) for p in ys if "===" in p]
  return ps[0:len(ps)-1]

def to_pair(xs):
  ys  = re.sub("===","",xs)
  ys  = ys.split(",")
  if len(ys) == 2:
    return (ys[0].strip(),ys[1].strip())

# read_total :: FilePath -> Float
def read_total(in_path):
  ps = fetch(in_path)
  for p in ps:
    if "cumulative occurrences" in p:
      m = p.replace("cumulative occurrences: ", "")
      n = m.split("\n")
      return float(n[0])


# # # # common read function

# @Input  : `path/to/file.extension`
# @Output : list where each element is a line from file
# fetch :: FilePath -> Eff [IO, Err String] [String]
def fetch(in_path):
    if os.path.exists(in_path):
      f  = open(in_path,'r')
      xs = f.read() 
      xs = xs.split(demark)
      ys = join([x.split('\n') for x in xs])
      return [y for y in ys if y]
    else:
      raise NameError("No file found for: " + in_path)


