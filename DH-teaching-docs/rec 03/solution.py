conj = float(input("How many conjugations?"))
det = float(input("How many determiners?"))
adj = float(input("How many adjectives?"))
prep = float(input("How many prepositions?"))
nouns = float(input("How many nouns?"))
adv = float(input("How many adverbs?"))
verbs = float(input("How many verbs?"))
totes = float(input("How many total words?"))

AVG_CONJ = .0415
AVG_DET = .1099
AVG_ADJ = .0603
AVG_PREP = .1184
AVG_NOUNS = .2049
AVG_ADV = .0604
AVG_VERBS = .1842

std_conj = .0104
std_det = .0256
std_adj = .0063
std_prep = .0184
std_nouns = .0278
std_adv = .0128
std_verbs = .0056

norm_conj = conj/totes
norm_det = det/totes
norm_adj = adj/totes
norm_prep = prep/totes
norm_nouns = nouns/totes
norm_adv = adv/totes
norm_verbs = verbs/totes

dev_conj = abs(norm_conj-AVG_CONJ)
dev_det = abs(norm_det-AVG_DET)
dev_adj = abs(norm_adj-AVG_ADJ)
dev_prep = abs(norm_prep-AVG_PREP)
dev_nouns = abs(norm_nouns-AVG_NOUNS)
dev_adv = abs(norm_adv-AVG_ADV)
dev_verbs = abs(norm_verbs-AVG_VERBS)

D_conj = dev_conj/std_conj
D_det = dev_det/std_det
D_adj = dev_adj/std_adj
D_prep = dev_prep/std_prep
D_nouns = dev_nouns/std_nouns
D_adv = dev_adv/std_adv
D_verbs = dev_verbs/std_verbs

print("Conjugations: normalized, %f; deviation from the mean, %f; delta %f." % (norm_conj,dev_conj,D_conj))
print("Determiners: normalized, %f; deviation from the mean, %f; delta %f." % (norm_det,dev_det,D_det))
print("Adjectives: normalized, %f; deviation from the mean, %f; delta %f." % (norm_adj,dev_adj,D_adj))
print("Prepositions: normalized, %f; deviation from the mean, %f; delta %f." % (norm_prep,dev_prep,D_prep))
print("Nouns: normalized, %f; deviation from the mean, %f; delta %f." % (norm_nouns,dev_nouns,D_nouns))
print("Adverbs: normalized, %f; deviation from the mean, %f; delta %f." % (norm_adv,dev_adv,D_adv))
print("Verbs: normalized, %f; deviation from the mean, %f; delta %f." % (norm_verbs,dev_verbs,D_verbs))







