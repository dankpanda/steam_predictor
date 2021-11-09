import pandas as pd

df = pd.read_csv('dataset/merged3.csv')



'''
df.drop_duplicates(subset=['name'],keep='last',inplace=True)
df.query('name != "-"',inplace=True)
df.query('user_reviews != "No user reviews"',inplace=True)
df = df[df['user_reviews'].str[-5:] != 'score']
df.query('all_reviews != "-"',inplace = True)
df.drop('img_url',axis=1,inplace=True)
df.drop('pegi_url',axis=1,inplace=True)
df.drop('user_reviews',axis=1,inplace=True)
for i in df.all_reviews:
    j = i.split()
    if j[-1] != "positive.":
        df.query('all_reviews != @i',inplace=True)

for i in df.index:
    review = df.at[i,'all_reviews']
    res = []
    review = review.replace('(',' ')
    review = review.replace(')',' ')
    review = review.replace(',','')
    review = review.replace('%','')
    review = review.split()
    for j in review:
        if len(res) < 2:
            try:
                value = int(j)
                res.append(int(j))
            except:
                continue
    df.at[i,'all_reviews'] = str(res[0]) + " " + str(res[1])

dropped = []
for i in df.index:
    
    a = df.at[i,'all_reviews']
    a = [int(i) for i in a.split()]
    if a[0] < 500:
        dropped.append(i)
df.drop(dropped,inplace=True)

df_text = pd.read_csv("dataset/text_content.csv")
df_merge = pd.merge(df,df_text,on="url")
df_merge.to_csv('dataset/final.csv',index=False)
df.drop('url',axis=1,inplace=True)
df.drop_duplicates(subset=['name'],keep='last',inplace=True)
df.query('name != "-"',inplace=True)
df.loc[df['price'].str[-4:] == 'Game', 'price'] = 'Free'

for i in df.index:
    price = df.at[i,'price']
    splitted = price.split()
    if splitted[-1][-8:] == 'Download':
        df.at[i,'price'] = 'Check store page'
        
    if "$Discount" in str(price) :
        df.at[i,'price'] = 'Check store page'
    if "subscription" in str(price).lower():
        df.at[i,'price'] = 'Check store page'
    if "NT$" in str(price).lower():
        df.at[i,'price'] = 'Check store page'

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
        res = res[::-1]
        df.at[i,'price'] = res

df['popu_tags'] = df['popu_tags'].str.replace('+', '')
df.drop('requirements',axis=1,inplace=True)
df.drop('desc',axis=1,inplace=True)
df.drop('full_desc',axis=1,inplace=True)
'''

categ_list = {'Online PVP','LAN PVP','Online Co-Op','LAN Co-Op','Cross-Platform','Multiplayer','Steam Workshop','In-App Purchases','Stats','MMO','Single-player','Steam Cloud','Captions available','Cross-Platform Multiplayer','Steam VR','Collectibles','Steam Leaderboards','Includes level editor','Downloadble Content'}
for i in df.index:
    categ = str(df.at[i,'categories'])
    



df.to_csv('dataset/merged3.csv',index=False)
