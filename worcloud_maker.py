import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import numpy as np
from preprocessor import lemmatize,remove_stopwords, get_dataframe_partitions
from sklearn.metrics import classification_report,accuracy_score,RocCurveDisplay,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import wordninja
import seaborn as sns

df = pd.read_csv("dataset/merged_preprocessed.csv")
df = df[df['review'].notna()]

def TF_IDF_most_used_words(category_string, data_series, palette, image_mask):
    #CHECKING OUT COMMON WORDS IN r/SuicideWatch USING TVEC
    tvec_optimised = TfidfVectorizer(max_df= 0.5, max_features=70, min_df=2, ngram_range=(1, 3),stop_words = 'english')
    tvec_optimised.fit(data_series)
    #CREATING A DATAFRAME OF EXTRACTED WORDS
    created_df = pd.DataFrame(tvec_optimised.transform(data_series).todense(),
                              columns=tvec_optimised.get_feature_names())
    total_words = created_df.sum(axis=0)
    
    #<<<WORDCLOUD>>>
    #CREATING A LONG STRING OF WORDS FOR THE WORD CLOUD MODULE
    top_40_words = total_words.sort_values(ascending = False).head(40)
    top_40_words_df = pd.DataFrame(top_40_words)
    top_words_cloud_df = top_40_words_df.reset_index()
    top_words_cloud_df.columns = ["words", "count"]
    one_string_list = []
    for i in range(len(top_words_cloud_df)):
        one_string = (top_words_cloud_df["words"][i] + " ")* (top_words_cloud_df["count"][i]).astype(int)
        one_string_list.append(one_string)
    long_string = " ".join(string for string in one_string_list)
    #print(long_string)
    # CREATING A WORD CLOUD IMAGE
    mask = np.array(Image.open(image_mask))
    wordcloud = WordCloud(repeat=True, collocations=False,min_font_size=2, max_font_size= 80, max_words= 10000, background_color= "white",colormap= palette,  mask= mask).generate(long_string)
    # DISPLAY IT
    #plt.axis("off")
    plt.figure(figsize = (20, 20), dpi=300)
    plt.title('\n{}\n'.format(category_string), fontsize=22)
    #plt.imshow(wordcloud, interpolation='bilinear') 
    image_colors = ImageColorGenerator(mask) #THIS MAKES THE WORDCLOUD RESPOND TO THE COLOURS IN THE MASK
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
    plt.axis("off")
    plt.show()
    
    #<<<BARPLOT>>>
    #CREATING A FINAL DATAFRAME OF THE TOP 20 WORDS
    top_20_words = total_words.sort_values(ascending = False).head(20)
    top_20_words_df = pd.DataFrame(top_20_words, columns = ["count"])
    #PLOTTING THE COUNT OF THE TOP 20 WORDS
    sns.set_style("white")
    plt.figure(figsize = (15, 8), dpi=300)
    ax = sns.barplot(y= top_20_words_df.index, x="count", data=top_20_words_df, palette = palette)
    
    plt.xlabel("Count", fontsize=9)
    plt.ylabel('Common Words in {}'.format(category_string), fontsize=9)
    plt.yticks(rotation=-5)
    plt.show()

TF_IDF_most_used_words("Words used by production model to identify r/SuicideWatch Posts", df['review'], "ocean", image_mask="assets/ending_mask_8.png")
