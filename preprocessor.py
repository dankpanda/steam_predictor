import nltk
import pandas as pd
from nltk.corpus import stopwords
import spacy
import numpy as np

# Lemmatizer
def lemmatize(dataframe):
    lemmatizer = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    for i in dataframe.index:
        print(i)
        cur = str(dataframe.at[i,'review'])
        lemmatized = lemmatizer(cur)
        dataframe.at[i,'review'] = " ".join(j.lemma_ for j in lemmatized)
    return dataframe
        
# Removing stopwords
def remove_stopwords(dataframe):
    stop = set(stopwords.words('english'))
    for i in dataframe.index:
        print(i)
        cur = str(dataframe.at[i,'review'])
        res = ""
        for j in cur.split():
            if(j not in stop):
                res += j 
                res += " "
        dataframe.at[i,'review'] = res 
    return dataframe



def get_dataframe_partitions(df, train_split = .8, val_split=.1, test_split=.1, seed=12):
  assert (train_split + test_split + val_split) == 1

  train, validate, test = np.split(df.sample(frac=1, random_state=seed), [int(train_split * len(df)), int((train_split + val_split)*len(df))])
  return train, validate, test