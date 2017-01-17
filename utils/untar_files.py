############################################################
# Module  : Untar all google ngram files
# Date    : November 15th
# Author  : Xiao Ling
############################################################


import gzip
import os


in_   = "/Users/lingxiao/Documents/research/code/good-great/LDC2006T13/data"
out   = "/Users/lingxiao/Documents/research/code/good-great/raw"


# @Use   : untar_all "path/to/input" "path/to/output"
# @Input : path to directory containing all google ngrams
#          path to another directory where untarred files
#          should be saved
# untar_all :: DirectoryPath -> DirectoryPath -> IO ()
def untar_all(in_,out):
	names = ['1gms', '2gms', '3gms', '4gms', '5gms']
	paths = [( os.path.join(in_, name)
		     , os.path.join(out, name)) \
	         for name in names]
	[untar_each(i,o) for (i,o) in paths]	     


# untar_each:: DirectoryPath -> DirectoryPath -> IO ()
def untar_each(indir, outdir):

	if not os.path.isdir(outdir):
		os.makedirs(outdir)

	files = os.listdir(indir)

	for afile in files:

		if afile.endswith('.gz'):

			name = os.path.splitext(afile)[0] + '.txt'
			inp  = os.path.join(indir , afile )
			outp = os.path.join(outdir, name  )

			with gzip.open(inp,'rb') as f:
				xs = f.read(f)
				o  = open(outp, 'w')
				o.write(xs)
				o.close()




