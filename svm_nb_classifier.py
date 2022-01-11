import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, RocCurveDisplay
from sklearn.naive_bayes import MultinomialNB
from data_utilities.preprocessor import get_dataframe_partitions
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn import svm
df = pd.read_csv('dataset/merged_df.csv')
df = df[df['review'].notna()]


train_df, val_df, test_df = get_dataframe_partitions(df,0.8,0.1,0.1)
x_train = train_df['review']
y_train = train_df['voted_up']
x_test = test_df['review']
y_test = test_df['voted_up']

svm = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', LinearSVC()),
              ])

svm.fit(x_train, y_train)
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(x_train, y_train)

from sklearn.metrics import classification_report

y_pred = nb.predict(x_test)
y_pred2 = svm.predict(x_test)
print(classification_report(y_test,y_pred))
print('Average accuracy: %s' % accuracy_score(y_test, y_pred))
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)
plt.show()

RocCurveDisplay.from_predictions(y_test,y_pred)
plt.plot([0, 1], [0, 1], 'k--')
plt.show()
print(classification_report(y_test,y_pred2))
print('Average accuracy: %s' % accuracy_score(y_test,y_pred2))
ConfusionMatrixDisplay.from_predictions(y_test,y_pred2)
plt.show()

RocCurveDisplay.from_predictions(y_test,y_pred2)
plt.plot([0, 1], [0, 1], 'k--')
plt.show()