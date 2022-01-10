import scattertext as st
import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
from preprocessor import lemmatize,remove_stopwords, get_dataframe_partitions
from sklearn.metrics import classification_report,accuracy_score,RocCurveDisplay,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from IPython.core.display import display, HTML
from scattertext import CorpusFromPandas, produce_scattertext_explorer
from IPython.display import IFrame

df = pd.read_csv("dataset/merged_preprocessed.csv")
df = df[df['review'].notna()]

scatter_data = df[['review', 'voted_up']]
scatter_data['category'] = scatter_data['voted_up'].map({0: 'Not Recommended', 1: 'Recommended'})
scatter_data.tail()
nlp = st.whitespace_nlp_with_sentences
scatter_data.groupby("category").apply(lambda x: x.review.apply(lambda x: len(x.split())).sum())
scatter_data['parsed'] = scatter_data.review.apply(nlp)
scatter_data.tail()
corpus = st.CorpusFromParsedDocuments(scatter_data, category_col="category", parsed_col="parsed").build()


html = st.produce_scattertext_explorer(corpus,
                                    category='Not Recommended',
                                    category_name='Not Recommended',
                                    not_category_name='Recommended',
                                    width_in_pixels=1000,
                                    jitter=0.1,
                                    minimum_term_frequency=5,
                                    transform=st.Scalers.percentile,
                                    metadata=scatter_data['category']
                                   )
file_name = 'assets/Reddit_ScattertextRankDataJitter.html'
open(file_name, 'wb').write(html.encode('utf-8'))
IFrame(src=file_name, width = 1200, height=700)