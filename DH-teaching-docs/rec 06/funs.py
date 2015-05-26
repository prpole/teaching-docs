from stopwords import *
from whartons_words import *

## Take two lists of words, remove stopwords, 
## generate list of bigrams, and return all common bigrams
# 
def main(list1,list2,stopwords):
	l1_stopped = remove_stopwords(list1,stopwords)
	l2_stopped = remove_stopwords(list2,stopwords)
	bigrams1 = ngrams(l1_stopped,2)
	bigrams2 = ngrams(l2_stopped,2)
	return list_intersection(bigrams1,bigrams2)

## Generate n from list of words
# @param words is a list of words
# @param words is length of gram, ie bigram is n=2
#
def ngrams(words,n):
	ngrams = []
	for i in range(len(words)-(n-1)):
		ngrams.append(words[i:i+n])
	return ngrams

## Return integer count of instances of word in text
# @param word is word to search for
# @param text is word to check for word in
#
def word_search(word,text):
	count = 0
	for n in text:
	    if n == word:
	        count += 1
	return count

## Return all common elements in list
#
def list_intersection(list1,list2):
	common = []
	for item1 in list1:
		if item1 in list2:
			common.append(item1)
	return common

## Given a text and a list of stopwords, remove stopwords from text
# @param text is list of words
# @param stopwords is list of stopwords
#
def remove_stopwords(text,stopwords):
	i = 0
	while i < len(text):
		if text[i].lower() in stopwords:
			text.remove(text[i])
		else:
			i += 1
	return text

print(main(hm_words,ef_words,stopwords))