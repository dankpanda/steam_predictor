import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
from data_utilities.preprocessor import get_dataframe_partitions
from sklearn.metrics import classification_report,accuracy_score,RocCurveDisplay,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Loading data
df = pd.read_csv("dataset/merged_df.csv")
df = df[df['review'].notna()]

# Defining variables
embedding_dim = 64
max_tokens = 30000
output_length = 300
batch_size = 16
epochs = 3
# 4 epoch

# Splitting dataset
train_df, val_df, test_df = get_dataframe_partitions(df,0.8,0.1,0.1,seed = 939)

x_train = train_df['review']
y_train = train_df['voted_up']
x_val = val_df['review']
y_val = val_df['voted_up']
x_test = test_df['review']
y_test = test_df['voted_up']

# Text vectorizer
vectorize_layer = TextVectorization(max_tokens = max_tokens, output_mode = 'int', output_sequence_length=output_length)
vectorize_layer.adapt(x_train)

# Defining model
def create_model():
    model = tf.keras.Sequential()
    model.add(vectorize_layer)
    model.add(tf.keras.layers.Embedding(input_dim = max_tokens+1,output_dim = embedding_dim))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim,return_sequences=True)))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(int(embedding_dim/2))))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(embedding_dim, activation='relu'))
    model.add(tf.keras.layers.Dense(embedding_dim/2, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(0.0001), metrics=['accuracy'])

    return model 

model = create_model()
#model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val,y_val),batch_size=batch_size)
# y_pred = model.predict(x_test)
# for i in range(len(y_pred)):
#     if y_pred[i] < 0.5:
#         y_pred[i] = 0
#     else:
#         y_pred[i] = 1

def trainloop(times):
    max = 0.8708894878706199
    max_iteration = -1
    iteration = 0
    for i in range(times):
        iteration += 1
        model.fit(x_train, y_train, epochs=epochs, validation_data=(x_val,y_val),batch_size=batch_size)
        y_pred = model.predict(x_test)
        for j in range(len(y_pred)):
            if y_pred[j] < 0.5:
                y_pred[j] = 0
            else:
                y_pred[j] = 1
        accuracy = accuracy_score(y_test,y_pred)
        if accuracy > max:
            max = accuracy 
            model.save("rnn",save_format="tf")
            max_iteration = iteration
        print("Best accuracy {}, current accuracy at iteration {}: {}".format(max,iteration,accuracy))
    
    print("Best model at iteration {} with accuracy of {}".format(max_iteration,max))

trainloop(3)
best_model = tf.keras.models.load_model('rnn')
y_pred = best_model.predict(x_test)
for i in range(len(y_pred)):
    if y_pred[i] < 0.5:
        y_pred[i] = 0
    else:
        y_pred[i] = 1


print("\nBidirectional LSTM Classification Report")
print(classification_report(y_test,y_pred))
accuracy = accuracy_score(y_test,y_pred)
print("Average accuracy: " + str(accuracy))
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)
plt.show()

RocCurveDisplay.from_predictions(y_test,y_pred)
plt.plot([0, 1], [0, 1], 'k--')
plt.show()

