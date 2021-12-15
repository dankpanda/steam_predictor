import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
nltk.download('wordnet')
import numpy as np

# Lemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatizeHelper(sentence):
    ret = []
    for i,j in pos_tag(word_tokenize(sentence)):
        res = j[0].lower()
        res = res if res in ['a','r','n','v'] else None
        if not res:
            lemma = i 
        else:
            lemma = lemmatizer.lemmatize(i,res)
        ret.append(lemma)
       
    return " ".join(ret)

def lemmatize(dataframe):
    for i in dataframe.index:
        dataframe.at[i,'review'] = lemmatizeHelper(dataframe.at[i,'review'])
    return dataframe

# Removing stopwords
stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def remove_stopwords(dataframe):
    dataframe['review'] = dataframe['review'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    return dataframe

def get_dataframe_partitions(df, train_split = .8, val_split=.1, test_split=.1, seed=12):
  assert (train_split + test_split + val_split) == 1

  train, validate, test = np.split(df.sample(frac=1, random_state=seed), [int(train_split * len(df)), int((train_split + val_split)*len(df))])
  return train, validate, test