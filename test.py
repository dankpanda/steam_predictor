import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
from sklearn import svm
df = pd.read_csv('dataset/merged_df.csv')
df = df[df['review'].notna()]
y = df.pop('voted_up').astype('int')
x = df['review']

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=558)
svc = svm.SVC()
svc.fit(x_train,y_train)
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(x_train, y_train)

from sklearn.metrics import classification_report

y_pred = nb.predict(x_test)
y_pred2 = svc.predict(x_test)
print(classification_report(y_test,y_pred))
print('Average accuracy: %s' % accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred2))
print('Average accuracy: %s' % accuracy_score(y_test,y_pred2))