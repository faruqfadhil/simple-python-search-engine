
# coding: utf-8

# In[1]:


import pandas
from numpy import genfromtxt
from spacy.lang.id import Indonesian

from sklearn.feature_extraction.text import TfidfVectorizer


# In[58]:


class SearchEngine:
    def __init__(self):
        self.nlp = Indonesian()
        self.nlp.Defaults.stop_words.update(genfromtxt('/media/faruq/FARUQ/PENS/semester6/datamining/program/django/ClassFormExample/newsletter/stopword.csv', dtype='|S18', delimiter=','))
        self.vectorizer = TfidfVectorizer(tokenizer=self.__tokenizer, ngram_range=(1, 1))
    
    def __tokenizer(self, text):
        return [token.lemma_.lower() for token in self.nlp(text) if not token.is_stop and not token.is_punct]
    
    def fit(self, dataset):
        self.dataset = dataset
        self.vector = self.vectorizer.fit_transform(self.dataset.article)
        
    def search(self, keyword, paginate=10, page=1):
        # Tokenize keyword
        keys = self.__tokenizer(keyword)
        
        # Find keyword in terms
        features = self.vectorizer.get_feature_names()
        vocabulary = self.vectorizer.vocabulary_
        key_indexes = [vocabulary[key] for key in keys if key in features]
        
        # Sum tfidf value
        tfidf = self.vector[:, key_indexes].toarray().sum(axis=1)
        tfidf = [[value.item()] for value in tfidf]
        
        # Sorting tfidf value
        tfidfDataFrame = pandas.DataFrame.from_records(tfidf, columns=["tfidf"])
        tfidfDataFrame = tfidfDataFrame.sort_values(by='tfidf', ascending=False)
        tfidfDataFrame.reset_index(inplace=True)
        
        # Selecting news
        start = paginate * (page - 1)
        end = start + paginate
        return self.dataset.iloc[tfidfDataFrame.iloc[start:end]['index']]
    
    def getVector(self):
        return self.vector
    
    def getVectorizer(self):
        return self.vectorizer


# #### Usage

# In[72]:


# df = pandas.read_csv("newsfeed.csv")


# In[60]:


# model = SearchEngine()
# model.fit(df)


# In[73]:


# anu = model.search("asian games jakarta")
# for index,row in anu.iterrows():
#     print(row['headline'])


