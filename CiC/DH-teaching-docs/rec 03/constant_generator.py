import nltk

filename = input("Enter filename (note: only works in file with pos_grab and files:")
name = filename
def wordSplitClean(myText,lower=False):
    puncMarks = [',', '.', '?', '!', ':', ';', '\'', '\"', '(', ')', '[', ']', '-']
    for item in puncMarks:
            myText = myText.replace(item, '')
    if lower:
        lowerText = myText.lower()
    	textWords = lowerText.split()
    else:
    	textWords = myText.split()
    return textWords

with open(filename,'r') as f:
    text = f.read()
tokes = wordSplitClean(text)
tagged = nltk.pos_tag(tokes)

def only_nouns(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['NN','NNS']:
            newtokes.append(tag[0])
    return newtokes

def only_adj(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['JJ','JJR','JJS']:
            newtokes.append(tag[0])
    return newtokes

def only_conj(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['CC']:
            newtokes.append(tag[0])
    return newtokes

def only_det(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['DT']:
            newtokes.append(tag[0])
    return newtokes

def only_prep(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['IN']:
            newtokes.append(tag[0])
    return newtokes

def only_adv(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['RB','RBR','RBS']:
            newtokes.append(tag[0])
    return newtokes

def only_verbs(filename):
    newtokes = []
    for tag in tagged:
        if tag[1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
            newtokes.append(tag[0])
    return newtokes

text_conj = only_conj(name)
text_det = only_det(name)
text_prep = only_prep(name)
text_adj = only_adj(name)
text_nouns = only_nouns(name)
text_adv = only_adv(name)
text_verbs = only_verbs(name)

print(name+' contains '+str(len(text_conj))+' conjugations.')

print(name+' contains '+str(len(text_det))+' determiners.')


print(name+' contains '+str(len(text_adj))+' adjectives.')
print(name+' contains '+str(len(text_prep))+' prepositions.')
print(name+' contains '+str(len(text_nouns))+' nouns.')
print(name+' contains '+str(len(text_adv))+' adverbs.')
print(name+' contains '+str(len(text_verbs))+' verbs.')
print(name+' contains '+str(len(tokes))+' total words.')


