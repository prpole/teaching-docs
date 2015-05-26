from whartons_words import *

ef_bigrams = []
hm_bigrams = []


for ndx,x in enumerate(ef_words):
	if ndx < len(ef_words)-1:
		bigram = [ef_words[ndx],ef_words[ndx+1]]
		ef_bigrams.append(bigram)

for ndx,x in enumerate(hm_words):
	if ndx < len(hm_words)-1:
		bigram = [hm_words[ndx],hm_words[ndx+1]]
		hm_bigrams.append(bigram)

print(ef_bigrams)
print()
print(hm_bigrams)