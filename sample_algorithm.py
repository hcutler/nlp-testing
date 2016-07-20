# Algorithm for discerning high level information about folks in the civic technology scene
# 1. Categorize sentences into one of the categories under consideration:
#     * Funding
#     * Data
#     * Employment
#     * Collaboration
#     * Location - from investigator
# 2. parse individual sentences once high level labels have been defined to do deep semantic analysis automatically
#    * We do this by pulling out the named entities and using the correct action words to imply causality
# 3. save to database
import spacy
import nltk
from spacy.parts_of_speech import *
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer #consider moving from CountVectorizer to this
from nltk.classify.scikitlearn import SklearnClassifier
# from text_classify.algorithms import *

def preprocess(sentence,label=None):
    tokens = nltk.word_tokenize(sentence)
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    features = {}
    for token in tokens:
        features[token]=tokens.count(token)
    if label:
        return (features,label)
    else:
        return features

def svm(train_data,preprocessing=True):
    training_data = []
    for data in train_data: 
        training_data.append(preprocess(data[0],label=data[1]))
    cl = SklearnClassifier(LinearSVC())
    cl.train(training_data)
    return cl

def tokenizeText(sample):
  tokens = sample.split(" ")
  # stoplist the tokens
  tokens = [tok for tok in tokens if tok not in STOPLIST]

  # stoplist symbols
  tokens = [tok for tok in tokens if tok not in SYMBOLS]

  # remove large strings of whitespace
  while "" in tokens:
      tokens.remove("")
  while " " in tokens:
      tokens.remove(" ")
  while "\n" in tokens:
      tokens.remove("\n")
  while "\n\n" in tokens:
      tokens.remove("\n\n")
  return tokens

# read in data file
with open("sample.txt","r") as f:
  data = f.read()

#sentence tokenization using spaCy
nlp = spacy.load("en")
d = data.decode('utf-8')
doc = nlp(d, tag=True) #tokenized doc
sentences = [sent.string.strip() for sent in doc.sents]


STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "..."]

# #ToDo fill in the labels your self!
labels = [] # funding
labels2 = [] # data
labels3 = [] # employment
labels4 = [] # collaboration
labels5 = [] # location


#Generate training set for each set of labels
training = zip(data,labels)
training2 = zip(data2, labels2)
training3 = zip(data2, labels2)
training4 = zip(data2, labels2)
training5 = zip(data2, labels2)

# create classifier for each training set
cl = svm(training) 
cl2 = svm(training2)
cl3 = svm(training3)
cl4 = svm(training4)
cl5 = svm(training5)

#test set - this will eventually be all of the Civicist/TP content?
test = preprocess("hello there friends")


# Now do something with the test set and each classifier??
# use something like "accuracy(cl, test)"?


