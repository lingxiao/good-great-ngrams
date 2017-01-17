############################################################
# Module  : normalize all google ngram files
# Date    : November 15th
# Author  : Xiao Ling
############################################################


import os


in_   = "/Users/lingxiao/Documents/research/data/ngrams/raw"
out   = "/Users/lingxiao/Documents/research/data/ngrams/normalized"

# @Use   : untar_all "path/to/input" "path/to/output"
# @Input : path to directory containing all google ngrams
#          path to another directory where untarred files
#          should be saved
# norm_all :: DirectoryPath -> DirectoryPath -> IO ()
def norm_all(in_,out):

	names = ['1gms']
	# names = ['2gms', '3gms', '4gms', '5gms']
	paths = [( os.path.join(in_, name)
		     , os.path.join(out, name)) \
	         for name in names]
	[norm_each(i,o) for (i,o) in paths]	     


# norm_each :: DirectoryPath -> DirectoryPath -> IO ()
def norm_each(indir, outdir):

	files = os.listdir(indir)

	for afile in files:

		if afile.endswith('.txt'):

			name = os.path.splitext(afile)[0] + '.txt'
			inp  = os.path.join(indir , afile )
			outp = os.path.join(outdir, name  )

			print ("==== normalizing file: " + inp)

			outf  = open(outp,'w')

			inf   = open(inp ,'r')	
			inf   = inf.read()
			lines = inf.split('\n')

			for line in lines:
				norm = line.lower().strip()
				outf.write(norm)
				outf.write('\n')

			outf.close()





