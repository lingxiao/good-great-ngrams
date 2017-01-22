############################################################
# Module  : Common Hsakell Prelude Functions
#          
# Date    : November 8th
# Author  : Xiao Ling
############################################################


############################################################
# List Operations
############################################################

# fmap :: (a -> b) -> [a] -> [b]
def fmap(g,xs):
	return [g(x) for x in xs]

# fold :: (a -> b -> b) -> b -> [a] -> b
def fold(g,y0,xs):
	y  = y0	
	for x in xs:
		y = g(x,y)
	return y

# zip_with :: (a -> b -> c) -> [a] -> [b] -> [c]
def zip_with(g, xs,ys):
	xys = zip(xs,ys)
	return [g(x,y) for (x,y) in xys]


# join [[a]] -> [a]
def join(xxs):
	return [item for sublist in xxs for item in sublist]


# any :: (a -> Bool) -> [a] -> Bool
def any_(g,xs):
	o = False
	for x in xs:
		o = o or g(x)
	return o

# chunks :: [a] -> Int -> [[a]]
def chunks(xs,n):
  for k in range(0,len(xs),n):
    yield xs[k:k+n]

















