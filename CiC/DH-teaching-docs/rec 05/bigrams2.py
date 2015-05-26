from whartons_words import *

bgs = []

for z,n in enumerate(ef_words):

	if z == len(ef_words)-1:
		pass
	else:
		bgn = [n,ef_words[z+1]]

		bgs.append(bgn)
print(bgs)