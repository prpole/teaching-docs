from whartons_words import *

x_words = ['the','lobster','eats','lobster']

for ndx,x in enumerate(x_words):
	if ndx < len(x_words)-1:
		print([x,x_words[ndx+1]])