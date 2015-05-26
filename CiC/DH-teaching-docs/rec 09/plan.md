#Check for successful installation

#Run through the assignment more or less

	- return another list of word frequencies
	- but now remove most common words

#teach list comprehensions

#plaintext corpus reader 

##without specifying tokenizer:

from nltk.corpus import PlaintextCorpusReader
corpus_root='/Users/phillippolefrone/Desktop/cic/student-papers/'
corp = PlaintextCorpusReader(corpus_root,'.*\.txt')

^^ explain syntax there

demonstrate: corp.words() corp.sents() corp.fileids()
crucial: corp.words(fileid) and corp.words([list,of,files])

But then be like, specify tokenizer

from nltk.tokenize import RegexpTokenizer
tokes = RegexpTokenizer('[A-z]\w+')
^^explain
wordlists = PlaintextCorpusReader(corpus_root,'.*\.txt',word_tokenizer=tokes)

#So then chuck some stuff in a list comprehension

[ w for w in corp.words('paper1.txt') if w not in corp.words(['paper2.txt','paper3.txt') ]

#FreqDist

from nltk.book import FreqDist
fdist = FreqDist(corp.words('paper1.txt'))

(#Remove words that are unique to your file

	- don't tell them this, but you can use a list composition to make a list of filenames that are not the current filename and feed that into corpusname.words() as an arg, then select only words that are in the list of words contained in those other filenames)

#stopwords

from nltk.corpus import stopwords as sw

swords = sw.words('english')
