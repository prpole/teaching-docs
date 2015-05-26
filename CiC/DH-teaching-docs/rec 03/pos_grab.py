import nltk

with open(filename,'r') as f:
    text = f.read()
tokes = nltk.tokenize.word_tokenize(text)
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