import pandas as pd
import os
#from langdetect import detect
from preprocessor import lemmatize, remove_stopwords
from string import punctuation
# #Initial merge
# merged_df = pd.DataFrame()
# csv_list = os.listdir('dataset')
# counter = 0
# for i in csv_list:
#     current_df = pd.read_csv('dataset/'+i)
#     current_df.query('votes_up > 10',inplace=True)
#     drop_list = ['language','votes_up','Unnamed: 0','recommendationid','timestamp_created','timestamp_updated','votes_funny','weighted_vote_score','comment_count','steam_purchase','received_for_free','written_during_early_access','author.steamid','author.num_games_owned','author.num_reviews','author.playtime_forever','author.playtime_last_two_weeks','author.playtime_at_review','author.last_played','timestamp_dev_responded','developer_response']
#     for i in drop_list:
#         try:
#             current_df.drop(i,axis=1,inplace=True)
#         except:
#             continue
#     merged_df = merged_df.append(current_df,ignore_index=True)
#     print(counter)
#     counter +=1

# merged_df.to_csv('dataset/merged_df.csv', index = False)
# print(merged_df.shape)

# # Converting all text to lower case
# df = pd.read_csv('dataset/merged_df.csv')
# for i in df.index:
#     cur = str(df.at[i,'review'])
#     cur = cur.lower()
#     df.at[i,'review'] = cur

# df.to_csv('merged_df.csv',index=False)

# # Removing special characters 1
# special_charas = ['\n','[i]','[/i]','[b]','[/b]','[spoiler]','[/spoiler]','[h1]','[/h1]','[h2]','[/h2]','[h3]','[/h3]','[u]','[/u]','[strike]','[/strike]','[noparse]','[/noparse]','[hr]','[/hr]','[/url]','[list]','[/list]','[*]','[url]','[table]','[/table]','[tr]','[/tr]','[tc]','[/tc]','[th]','[/th]','[quote]','[/quote]','[td]','[/td]','[code]','[/code]']
# df = pd.read_csv('dataset/merged_df.csv')

# counter = 0
# for i in df.index:
#     cur = str(df.at[i,'review'])
#     for j in special_charas:
#         if(j == special_charas[0]):
#             cur = cur.replace(str(j),' ')
#             cur=cur.replace(str(j.upper()),' ')
#         cur=cur.replace(str(j),'')
#         cur = cur.replace(str(j.upper()),'')
#     df.at[i,'review'] = cur 
#     print(counter)
#     counter += 1

# df.to_csv("merged_df.csv",index=False)

# # Removing special characters 2 (urls)
# df = pd.read_csv('dataset/merged_df.csv')
# for i in df.index:
#     review = str(df.at[i,'review'])
#     temp = review.split('[url=')
#     if(len(temp) > 1):
#         cur = ""
#         for j in temp: 
#             if j == temp[0]:
#                 cur += j 
#             else:
#                 ind = 0
#                 for k in j:
#                     if k == ']':
#                         cur += j[ind+1:]
#                     ind += 1
#         df.at[i,'review'] = cur
    

# df.to_csv('merged_df.csv',index = False)

# # Remove other urls
# df = pd.read_csv('dataset/merged_df.csv')
# for i in df.index:
#     print(i)
#     res = ""
#     for j in str(df.at[i,'review']).split():
#         if j[:4] != "http":
#             res += j 
#             res += " "
#     df.at[i,'review'] = res

# df.to_csv('merged_df.csv',index=False)

# # Converting TRUE and FALSE to 0 and 1
# df = pd.read_csv('dataset/merged_df.csv')
# df['voted_up'] = df['voted_up'].astype("string")
# for i in df.index:
#     if df.at[i,'voted_up'] == 'True':
#         df.at[i,'voted_up'] = '1'
#     else: 
#         df.at[i,'voted_up'] = '0'
# df['voted_up'] = df['voted_up'].astype(int)
# df.to_csv('merged_df.csv',index=False)


# # Removing non ascii characters
# df = pd.read_csv('dataset/merged_df.csv')
# for i in df.index:
#     cur = str(df.at[i,'review'])
#     if(cur.isascii() == False):
#         for j in cur:
#             if(j.isascii() == False):
#                 cur = cur.replace(j, '')
#         df.at[i,'review'] = cur
# df.to_csv('merged_df.csv',index=False)

# # Removing non english rows
# df = pd.read_csv('dataset/merged_df.csv')
# drop_index=[]
# for i in df.index:
#     try:
#         language = detect(str(df.at[i,'review']))
#     except:
#         print(df.iloc[[i]].review)
#         language = '?'
#     if language != 'en':
#         drop_index.append(i)

# print(df.shape)
# df.drop(drop_index,inplace=True)
# print(df.shape)
# df.to_csv('merged_df.csv',index=False)

# #Removing stopwords
# df = pd.read_csv('dataset/merged_df.csv')
# df = remove_stopwords(df)
# df.to_csv('merged_df.csv',index=False)

# # Lemmatization 
# df = pd.read_csv('dataset/merged_df.csv')
# df = lemmatize(df)
# df.to_csv('merged_df.csv',index=False)



# Removing punctuations
# punct = {}
# for i in punctuation:
#   if i == "'":
#       punct[ord(i)] = None
#   else:
#       punct[ord(i)] = 32

# df = pd.read_csv('dataset/merged_df.csv')
# for i in df.index:
#     print(i)
#     temp = str(df.at[i,'review']).translate(punct).split() 
#     df.at[i,'review'] = " ".join(temp)

# df.to_csv('merged_df.csv',index=False)

