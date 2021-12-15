import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
from preprocessor import lemmatize,remove_stopwords, get_dataframe_partitions
from sklearn.metrics import classification_report,accuracy_score,r2_score
import matplotlib.pyplot as plt
# Loading data
df = pd.read_csv("merged_df.csv")
df = df[df['review'].notna()]

# Defining variables
embedding_dim = 128
max_tokens = 10000
output_length = 150
epochs = 10

# # Data preprocessing
# df = lemmatize(df)
# df = remove_stopwords(df)

df = pd.read_csv("merged_preprocessed.csv")
df = df[df['review'].notna()]
df = df.head(5000)
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
    model.add(tf.keras.layers.Embedding(input_dim = max_tokens+1,output_dim = embedding_dim,mask_zero = True))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim))),
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(embedding_dim, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(embedding_dim/2, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(embedding_dim/4, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(1))
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(0.0001), metrics=['accuracy'])

    return model 

model = create_model()
history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val,y_val))
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

# Uncomment the following blocks of code to generate graph
# Plot for accuracy
plt.rc('xtick', labelsize = 12)
plt.rc('ytick',labelsize = 12)
fig = plt.figure()
acc = fig.add_subplot(1,2,1)
acc.plot(history.history['accuracy'])
acc.plot(history.history['val_accuracy'])
acc.set_aspect(1.0/acc.get_data_ratio())
acc.set_title('model accuracy',fontsize= 15)
acc.set_ylabel('accuracy',fontsize = 15)
acc.set_xlabel('epoch', fontsize = 15)
acc.legend(['train', 'eval'], loc='upper left',fontsize = 12)
# # Plot for loss
loss = fig.add_subplot(1,2,2)
loss.plot(history.history['loss'])
loss.plot(history.history['val_loss'])
loss.set_aspect(1.0/loss.get_data_ratio())
loss.set_title('model loss',fontsize = 15)
loss.set_ylabel('loss',fontsize = 15)
loss.set_xlabel('epoch',fontsize=15)
fig.show()


    


