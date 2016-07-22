# Hypothesis Testing: Data Automation for Civic Graph

## In this repo:
* Testing different NLP tools (spaCy, nltk and others) to analyze corpus of blog content about civic tech
* Algorithm for discerning high level information about folks in the civic technology scene
    * Sentence tokenization of training data -> // TODO
    * Categorize each training dataset as having or not having a particular label (funding, data, employment, collaboration, location) -> // TODO
    * Create classifier for each label using a Support Vector Machine 


## To do:
* Find training datasets (one for each classifier)
      * Sentence tokenize training data
      * Manually label sentences in each training dataset (1: has label , 0: doesn't have label)
* Run each classifier on test data
* Parse sentences once labels have been defined to do Named Entity Recognition (NER) and use the correct action words to imply causality (on training? on test?)
* Save results to database (create new schema or pipe directly to Civic Graph)?
* Design pipeline to Civic Graph backend
* Include pipeline diagram in repo


## Tools used:
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [spaCy](https://spacy.io/docs)
* [nltk](http://www.nltk.org/book/)
* [scikit-learn](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)

## Exploring:
* [Bing Knowledge Widget](https://www.bing.com/partners/developers#BingSearchApi)
* [Wikipedia API](https://pypi.python.org/pypi/wikipedia/)
* [Wikidata package](https://pypi.python.org/pypi/wikidata_suggest/0.0.6)
* [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/)

## Have not used but plan to explore:
* [textacy](https://pypi.python.org/pypi/textacy)
