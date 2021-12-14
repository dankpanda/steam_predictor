import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/merged_df.csv')

y = df.pop('voted_up')
x = df['review']

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=69420)

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(x_train, y_train)

from sklearn.metrics import classification_report
y_pred = nb.predict(x_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))