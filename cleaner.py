import pandas as pd
import os

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

# # Removing special characters 1
# special_charas = ['\n','[i]','[/i]','[b]','[/b]','[spoiler]','[/spoiler]','[h1]','[/h1]','[h2]','[/h2]','[h3]','[/h3]','[u]','[/u]','[strike]','[/strike]','[noparse]','[/noparse]','[hr]','[/hr]','[/url]','[list]','[/list]','[*]','[url]','[table]','[/table]','[tr]','[/tr]','[tc]','[/tc]','[th]','[/th]','[quote]','[/quote]','[td]','[/td]']
# df = pd.read_csv('dataset/merged_df.csv')

# counter = 0
# for i in df.index:
#     cur = str(df.at[i,'review'])
#     for j in special_charas:
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

df = pd.read_csv('merged_df.csv')
df['review'] = df['review'].astype("string")
df.to_csv('merged_df.csv',index=False)
print(df.dtypes)