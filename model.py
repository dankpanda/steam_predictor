import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
from preprocessor import lemmatize,remove_stopwords, get_dataframe_partitions
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt
# Loading data
df = pd.read_csv("merged_df.csv")
df = df[df['review'].notna()]

# Defining variables
embedding_dim = 64
max_tokens = 30000
output_length = 300
epochs = 10
# 4 epoch
    
# # Data preprocessing
# df = lemmatize(df)
# df = remove_stopwords(df)

df = pd.read_csv("merged_preprocessed.csv")
df = df[df['review'].notna()]

# Splitting dataset
train_df, val_df, test_df = get_dataframe_partitions(df,0.7,0.15,0.15)

x_train = train_df['review']
y_train = train_df['voted_up']
x_val = val_df['review']
y_val = val_df['voted_up']
x_test = test_df['review']
y_test = test_df['voted_up']

# Text vectorizer
vectorize_layer = TextVectorization(max_tokens = max_tokens, output_mode = 'int', output_sequence_length=output_length)
vectorize_layer.adapt(x_train)
# vocab = vectorize_layer.get_vocabulary()
# print(vocab[:20])

# Defining model
def create_model():
    model = tf.keras.Sequential()
    model.add(vectorize_layer)
    model.add(tf.keras.layers.Embedding(input_dim = max_tokens,output_dim = embedding_dim))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)))
    model.add(tf.keras.layers.Dense(embedding_dim))
    model.add(tf.keras.layers.Dense(1))
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer='adam', metrics=['accuracy'])

    return model 

model = create_model()
history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val,y_val),batch_size=16)
y_pred = model.predict(x_test)
for i in range(len(y_pred)):
    if y_pred[i] < 0.5:
        y_pred[i] = 0
    else:
        y_pred[i] = 1
print("\nBidirectional LSTM Classification Report")
print(classification_report(y_test,y_pred))
accuracy = accuracy_score(y_test,y_pred)
print("Average accuracy: " + str(accuracy))
