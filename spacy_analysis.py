#ENTITY RECOGNITION
#ENTITY RECOGNITION

with open("all_content-COMBINED.txt","r") as f:
  data = f.read() # type 'string'

#spacy
import spacy
from spacy.attrs import ORTH, LIKE_URL, IS_OOV, NORM
import operator
from operator import itemgetter
from collections import OrderedDict

nlp = spacy.load("en")
d = data.decode('utf-8')
doc = nlp(d) #tokens


#count up entity frequencies and sort list in ascending order by value
ents = list(doc.ents)

counts = {}
for e in ents:
  e = str(e)
  if e in counts.keys():
    counts[e] += 1
  else:
    counts[e] = 1

d_sorted_by_value = OrderedDict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

for k, v in d_sorted_by_value.items():
  print "%s: %s" % (k, v)




# for e in ents:
#   #print(e.label, e.label_, ' '.join(t.orth_ for t in e))
#   print type(' '.join(t.orth_ for t in e))


# counts = {}

# counts = doc.count_by(ents.orth_)
# print counts


# import code
# code.interact(local=locals())

#textacy


#nltk