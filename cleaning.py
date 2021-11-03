import pandas as pd

# Initial merge
''' 
df_numeric = pd.read_csv("steam_data.csv")
df_text = pd.read_csv("text_content.csv")

df_games = pd.merge(df_numeric,df_text,on="url")
df_games.drop_duplicates(inplace=True)
df_games.to_csv("merged_data.csv")
'''

df = pd.read_csv('dataset/merged_data.csv')
# Dropping columns

'''
df.drop('img_url',inplace=True,axis=1)
df.drop('all_reviews',inplace=True,axis=1)
df.drop('url',inplace=True,axis=1)
df.drop('pegi_url',inplace=True,axis=1)
'''

# Cleaning rows
'''
df.drop_duplicates(subset=['name'],keep='last',inplace=True)
df['full_desc'] = df['full_desc'].str[15:]
df.query('name != "-"',inplace=True)
df = df[df['user_reviews'].str[-5:] != 'score']
df.query('user_reviews != "No user reviews"',inplace=True)
df.loc[df['price'].str[-4:] == 'Game', 'price'] = 'Free'
'''
# TODO FIX FOR FUCKING TAIWANESE DOLLARS AND MAYBE EVEN SOME OTHER CURRENCY
for i in df.index:
    if df.at[i,'price'][-4:] in ['Cart','more']: 
        price = df.at[i,'price']
        res = ""
        price = price.split('Add to Cart')[0]
        for j in price[::-1]:
            if j != "$":
                res += j
            else:
                break
        res += "$"
        res = res[::-1]
        df.at[i,'price'] = res

df.to_csv("dataset/merged_data2.csv",index=False)
