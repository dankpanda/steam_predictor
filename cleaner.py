import pandas as pd
from encoder import encode, calcValue
df = pd.read_csv('dataset/merged2.csv')



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

for i in df.index:
    tags = df.at[i,'popu_tags']
    for j in tag_list:
        wordIndex = tags.find(j)
        if wordIndex >0 :
            tags = tags[:wordIndex] +',' + tags[wordIndex:]
    df.at[i,'popu_tags'] = tags
tag_list = ['Indie', 'Action', 'Adventure', 'Casual', 'Simulation', 'Strategy', 'RPG', 'Singleplayer', 'Early Access', 'Free to Play', '2D', 'Atmospheric', 'Violent', 'Sports', 'Massively Multiplayer', 'Multiplayer', 'Puzzle', 'Story Rich', '3D', 'Fantasy', 'Pixel Graphics', 'Colorful', 'Racing', 'Nudity', 'Gore', 'Sexual Content', 'Exploration', 'Cute', 'Anime', 'First-Person', 'Funny', 'Sci-fi', 'Arcade', 'Shooter', 'Horror', 'Family Friendly', 'Retro', 'Great Soundtrack', 'Relaxing', 'Open World', 'Action-Adventure', 'Co-op', 'Platformer', 'Survival', 'Female Protagonist', 'Difficult', 'Combat', 'Third Person', 'VR', 'Comedy', 'Old School', 'Stylized', 'PvP', 'FPS', 'Visual Novel', 'Online Co-Op', 'Choices Matter', 'Realistic', 'Controller', 'Physics', 'Top-Down', 'Dark', 'Mystery', 'Character Customization', 'Sandbox', 'Cartoony', "Shoot 'Em Up", 'Psychological Horror', 'Multiple Endings', 'Tactical', 'Design & Illustration', '2D Platformer', 'PvE', 'Minimalist', 'Space', 'Building', 'Utilities', 'Point & Click', 'Linear', 'Local Multiplayer', 'Futuristic', 'Management', 'Magic', 'Action RPG', '1980s', 'Crafting', 'Hand-drawn', 'Turn-Based', 'Side Scroller', 'Education', 'Replay Value', 'Procedural Generation', 'Cartoon', 'Medieval', 'Puzzle Platformer', 'Resource Management', 'Survival Horror', 'Mature', 'Zombies', 'War', 'Local Co-Op', 'Logic', 'Turn-Based Strategy', 'Roguelike', 'Turn-Based Combat', 'Dark Fantasy', 'Drama', 'Hack and Slash', 'Romance', 'Post-apocalyptic', '3D Platformer', 'Choose Your Own Adventure', 'Base Building', 'Memes', 'Historical', 'Roguelite', 'Turn-Based Tactics', 'Dating Sim', 'JRPG', 'Stealth', 'Web Publishing', 'Interactive Fiction', 'Walking Simulator', 'Surreal', 'Hidden Object', 'Narration', 'Classic', 'Dungeon Crawler', 'Party-Based RPG', 'Fast-Paced', 'Emotional', 'Military', 'Short', 'Score Attack', 'Bullet Hell', 'Movie', 'Third-Person Shooter', 'Hentai', "1990's", 'Nature', 'Software', 'Animation & Modeling', 'Immersive Sim', 'Team-Based', 'RTS', 'Robots', 'Top-Down Shooter', 'Isometric', 'Cyberpunk', 'Dark Humor', 'Beautiful', 'Text-Based', '2.5D', 'Aliens', 'Conversation', 'Experimental', 'Cinematic', 'Driving', 'Economy', 'Music', 'RPGMaker', 'Card Game', 'Fighting', 'Abstract', 'LGBTQ+', 'Investigation', '4 Player Local', 'Action Roguelike', 'Tutorial', 'Inventory Management', 'Nonlinear', 'Flight', 'Board Game', 'Perma Death', 'Tabletop', 'Audio Production', 'Soundtrack', 'Thriller', 'Detective', 'Real Time Tactics', 'Artificial Intelligence', 'Psychological', 'Arena Shooter', 'Strategy RPG', 'Moddable', 'Demons', 'Video Production', 'Tower Defense', 'NSFW', 'Competitive', 'Modern', 'Clicker', 'Life Sim', 'Lore-Rich', 'City Builder', 'Psychedelic', 'Destruction', 'Dystopian', "Beat 'em up", 'Loot', 'Time Management', 'Precision Platformer', 'Metroidvania', 'Supernatural', 'Tactical RPG', 'Alternate History', 'Level Editor', 'Wargame', 'Comic Book', 'MMORPG', 'Game Development', 'Crime', 'Parkour', 'Souls-like', 'Character Action Game', 'Dark Comedy', 'World War II', 'Mythology', '2D Fighter', 'Runner', 'Grid-Based Movement', 'Philosophical', 'CRPG', 'Science', 'Twin Stick Shooter', 'Addictive', 'Automobile Sim', 'Co-op Campaign', 'Software Training', 'Class-Based', 'Grand Strategy', 'Space Sim', 'Blood', 'Gun Customization', 'Rhythm', 'Swordplay', 'Collectathon', 'Lovecraftian', 'Split Screen', 'Idler', 'Battle Royale', 'Cats', 'Illuminati', 'Open World Survival Craft', 'Dragons', 'Match 3', 'Deckbuilding', 'eSports', '6DOF', '3D Vision', 'Vehicular Combat', 'America', 'Parody', 'Noir', 'Card Battler', 'Conspiracy', 'Satire', '3D Fighter', 'Bullet Time', 'Capitalism', 'Trading', 'Voxel', 'Real-Time', 'Mouse only', 'Episodic', 'Political', 'Steampunk', 'Cult Classic', 'Epic', 'Photo Editing', 'Time Manipulation', 'Colony Sim', 'Mechs', 'Automation', 'Mystery Dungeon', 'Hunting', 'Gothic', 'Time Travel', 'Mining', 'Underground', 'Agriculture', 'Tanks', 'Dynamic Narration', 'Remake', 'MOBA', 'Otome', 'Politics', 'Farming Sim', 'Hacking', 'Ninja', 'Martial Arts', 'Quick-Time Events', 'Pirates', 'Word Game', 'God Game', 'Hero Shooter', 'Dog', 'Hex Grid', 'Spectacle fighter', 'Cold War', 'FMV', '4X', 'Solitaire', 'Asynchronous Multiplayer', 'Combat Racing', 'Looter Shooter', 'Fishing', 'Superhero', 'Trading Card Game', 'Creature Collector', 'Real-Time with Pause', 'Dinosaurs', 'Programming', 'Assassin', 'Underwater', 'Trains', 'Vampire', 'Naval', 'Kickstarter', 'Heist', 'Western', 'Immersive', 'Minigames', 'Narrative', 'Faith', 'Sokoban', 'Political Sim', 'GameMaker', 'Party', 'Archery', 'Touch-Friendly', 'Cooking', 'Experience', 'Diplomacy', 'Party Game', 'Mod', 'Foreign', 'Transportation', 'Snow', 'Sequel', 'Naval Combat', 'Auto Battler', 'Dungeons & Dragons', 'Documentary', 'Sailing', 'Music-Based Procedural Generation', 'Time Attack', 'Sniper', 'Games Workshop', 'Soccer', 'Transhumanism', 'Villain Protagonist', 'Gambling', 'Mars', 'World War I', 'Typing', 'Football', 'On-Rails Shooter', 'Offroad', 'Horses', 'Action RTS', 'Gaming', 'Werewolves', 'Silent Protagonist', 'Trivia', 'Crowdfunded', '360 Video', 'Chess', 'Nostalgia', 'Farming', 'Boxing', 'Traditional Roguelike', 'Unforgiving', 'LEGO', 'TrackIR', 'Roguelike Deckbuilder', 'Jet', 'Pinball', 'Outbreak Sim', 'Spaceships', 'Rome', 'Electronic Music', 'Golf', 'Motorbike', 'Ambient', 'Medical Sim', 'Asymmetric VR', 'Warhammer 40K', 'Based On A Novel', 'Spelling', 'Submarine', 'Bikes', 'Basketball', 'Roguevania', 'Escape Room', 'Social Deduction', 'Mini Golf', 'Intentionally Awkward Controls', 'Instrumental Music', 'Wrestling', 'Pool', 'Skateboarding', 'Vikings', 'Lemmings', 'Benchmark', 'Steam Machine', 'Baseball', 'Tennis', 'Hardware', 'Hockey', 'Skating', 'Electronic', 'Bowling', 'Cycling', 'Motocross', 'Rock Music', 'Feature Film', 'Voice Control', '8-bit Music', 'ATV', 'Well-Written', 'BMX', 'Skiing', 'Snowboarding', 'Boss Rush', 'Reboot']


df.drop('pegi',axis = 1, inplace=True)
df.drop('categories',axis = 1, inplace=True)
df.drop('popu_tags',axis = 1, inplace = True)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in df.index:
    fullDate = str(df.at[i,'date'])
    if fullDate[:3] in months and '-' not in fullDate:
        month = months.index(fullDate[:3])+1
        date = fullDate.split()[1][:-1]
        year = fullDate.split()[-1]
        df.at[i,'date'] = str(date) + '/' + str(month) + '/' + year     
categ_list = {'Indie', 'Action', 'Adventure', 'Casual', 'Simulation', 'Strategy', 'RPG', 'Singleplayer', 'Early Access', 'Free to Play', '2D', 'Atmospheric', 'Violent', 'Sports', 'Massively Multiplayer', 'Multiplayer', 'Puzzle', 'Story Rich', '3D', 'Fantasy', 'Pixel Graphics', 'Colorful', 'Racing', 'Nudity', 'Gore', 'Sexual Content', 'Exploration', 'Cute', 'Anime', 'First-Person', 'Funny', 'Sci-fi', 'Arcade', 'Shooter', 'Horror', 'Family Friendly', 'Retro', 'Great Soundtrack', 'Relaxing', 'Open World', 'Action-Adventure', 'Co-op', 'Platformer', 'Survival', 'Female Protagonist', 'Difficult', 'Combat', 'Third Person', 'VR', 'Comedy', 'Old School', 'Stylized', 'PvP', 'FPS', 'Visual Novel', 'Online Co-Op', 'Choices Matter', 'Realistic', 'Controller', 'Physics', 'Top-Down', 'Dark', 'Mystery', 'Character Customization', 'Sandbox', 'Cartoony', "Shoot 'Em Up", 'Psychological Horror', 'Multiple Endings', 'Tactical', 'Design & Illustration', '2D Platformer', 'PvE', 'Minimalist', 'Space', 'Building', 'Utilities', 'Point & Click', 'Linear', 'Local Multiplayer', 'Futuristic', 'Management', 'Magic', 'Action RPG', '1980s', 'Crafting', 'Hand-drawn', 'Turn-Based', 'Side Scroller', 'Education', 'Replay Value', 'Procedural Generation', 'Cartoon', 'Medieval', 'Puzzle Platformer', 'Resource Management', 'Survival Horror', 'Mature', 'Zombies', 'War', 'Local Co-Op', 'Logic', 'Turn-Based Strategy', 'Roguelike', 'Turn-Based Combat', 'Dark Fantasy', 'Drama', 'Hack and Slash', 'Romance', 'Post-apocalyptic', '3D Platformer', 'Choose Your Own Adventure', 'Base Building', 'Memes', 'Historical', 'Roguelite', 'Turn-Based Tactics', 'Dating Sim', 'JRPG', 'Stealth', 'Web Publishing', 'Interactive Fiction', 'Walking Simulator', 'Surreal', 'Hidden Object', 'Narration', 'Classic', 'Dungeon Crawler', 'Party-Based RPG', 'Fast-Paced', 'Emotional', 'Military', 'Short', 'Score Attack', 'Bullet Hell', 'Movie', 'Third-Person Shooter', 'Hentai', "1990's", 'Nature', 'Software', 'Animation & Modeling', 'Immersive Sim', 'Team-Based', 'RTS', 'Robots', 'Top-Down Shooter', 'Isometric', 'Cyberpunk', 'Dark Humor', 'Beautiful', 'Text-Based', '2.5D', 'Aliens', 'Conversation', 'Experimental', 'Cinematic', 'Driving', 'Economy', 'Music', 'RPGMaker', 'Card Game', 'Fighting', 'Abstract', 'LGBTQ+', 'Investigation', '4 Player Local', 'Action Roguelike', 'Tutorial', 'Inventory Management', 'Nonlinear', 'Flight', 'Board Game', 'Perma Death', 'Tabletop', 'Audio Production', 'Soundtrack', 'Thriller', 'Detective', 'Real Time Tactics', 'Artificial Intelligence', 'Psychological', 'Arena Shooter', 'Strategy RPG', 'Moddable', 'Demons', 'Video Production', 'Tower Defense', 'NSFW', 'Competitive', 'Modern', 'Clicker', 'Life Sim', 'Lore-Rich', 'City Builder', 'Psychedelic', 'Destruction', 'Dystopian', "Beat 'em up", 'Loot', 'Time Management', 'Precision Platformer', 'Metroidvania', 'Supernatural', 'Tactical RPG', 'Alternate History', 'Level Editor', 'Wargame', 'Comic Book', 'MMORPG', 'Game Development', 'Crime', 'Parkour', 'Souls-like', 'Character Action Game', 'Dark Comedy', 'World War II', 'Mythology', '2D Fighter', 'Runner', 'Grid-Based Movement', 'Philosophical', 'CRPG', 'Science', 'Twin Stick Shooter', 'Addictive', 'Automobile Sim', 'Co-op Campaign', 'Software Training', 'Class-Based', 'Grand Strategy', 'Space Sim', 'Blood', 'Gun Customization', 'Rhythm', 'Swordplay', 'Collectathon', 'Lovecraftian', 'Split Screen', 'Idler', 'Battle Royale', 'Cats', 'Illuminati', 'Open World Survival Craft', 'Dragons', 'Match 3', 'Deckbuilding', 'eSports', '6DOF', '3D Vision', 'Vehicular Combat', 'America', 'Parody', 'Noir', 'Card Battler', 'Conspiracy', 'Satire', '3D Fighter', 'Bullet Time', 'Capitalism', 'Trading', 'Voxel', 'Real-Time', 'Mouse only', 'Episodic', 'Political', 'Steampunk', 'Cult Classic', 'Epic', 'Photo Editing', 'Time Manipulation', 'Colony Sim', 'Mechs', 'Automation', 'Mystery Dungeon', 'Hunting', 'Gothic', 'Time Travel', 'Mining', 'Underground', 'Agriculture', 'Tanks', 'Dynamic Narration', 'Remake', 'MOBA', 'Otome', 'Politics', 'Farming Sim', 'Hacking', 'Ninja', 'Martial Arts', 'Quick-Time Events', 'Pirates', 'Word Game', 'God Game', 'Hero Shooter', 'Dog', 'Hex Grid', 'Spectacle fighter', 'Cold War', 'FMV', '4X', 'Solitaire', 'Asynchronous Multiplayer', 'Combat Racing', 'Looter Shooter', 'Fishing', 'Superhero', 'Trading Card Game', 'Creature Collector', 'Real-Time with Pause', 'Dinosaurs', 'Programming', 'Assassin', 'Underwater', 'Trains', 'Vampire', 'Naval', 'Kickstarter', 'Heist', 'Western', 'Immersive', 'Minigames', 'Narrative', 'Faith', 'Sokoban', 'Political Sim', 'GameMaker', 'Party', 'Archery', 'Touch-Friendly', 'Cooking', 'Experience', 'Diplomacy', 'Party Game', 'Mod', 'Foreign', 'Transportation', 'Snow', 'Sequel', 'Naval Combat', 'Auto Battler', 'Dungeons & Dragons', 'Documentary', 'Sailing', 'Music-Based Procedural Generation', 'Time Attack', 'Sniper', 'Games Workshop', 'Soccer', 'Transhumanism', 'Villain Protagonist', 'Gambling', 'Mars', 'World War I', 'Typing', 'Football', 'On-Rails Shooter', 'Offroad', 'Horses', 'Action RTS', 'Gaming', 'Werewolves', 'Silent Protagonist', 'Trivia', 'Crowdfunded', '360 Video', 'Chess', 'Nostalgia', 'Farming', 'Boxing', 'Traditional Roguelike', 'Unforgiving', 'LEGO', 'TrackIR', 'Roguelike Deckbuilder', 'Jet', 'Pinball', 'Outbreak Sim', 'Spaceships', 'Rome', 'Electronic Music', 'Golf', 'Motorbike', 'Ambient', 'Medical Sim', 'Asymmetric VR', 'Warhammer 40K', 'Based On A Novel', 'Spelling', 'Submarine', 'Bikes', 'Basketball', 'Roguevania', 'Escape Room', 'Social Deduction', 'Mini Golf', 'Intentionally Awkward Controls', 'Instrumental Music', 'Wrestling', 'Pool', 'Skateboarding', 'Vikings', 'Lemmings', 'Benchmark', 'Steam Machine', 'Baseball', 'Tennis', 'Hardware', 'Hockey', 'Skating', 'Electronic', 'Bowling', 'Cycling', 'Motocross', 'Rock Music', 'Feature Film', 'Voice Control', '8-bit Music', 'ATV', 'Well-Written', 'BMX', 'Skiing', 'Snowboarding', 'Boss Rush', 'Reboot','Online PvP','LAN PvP','Online Co-op','LAN Co-op','Cross-Platform Multiplayer','Steam Workshop','In-App Purchases','Stats','MMO','Single-player','Steam Cloud','Captions available','Cross-Platform Multiplayer','Steam VR','Collectibles','Steam Leaderboards','Includes level editor','Downloadable Content','Shared/Split Screen Co-op','Shared/Split Screen PvP','Captions available'}

from datetime import datetime
for i in df.index:
    date = df.at[i,'date']
    date = [int(x) for x in date.split("/")]
  
    dayOfYear = datetime(date[-1],date[1],date[0]).timetuple().tm_yday
    df.at[i,'year'] = date[-1]
    df.at[i,'day'] = dayOfYear
for i in df.index:
    categ = str(df.at[i,'categories']).split(',')
    popu_tag = str(df.at[i,'popu_tags']).split(',')
    joined = set(categ+popu_tag)
    res = ''
    for j in joined:
        if j != '':
            res += j + ','
    res = res[:-1]
    df.at[i,'tags'] = res

for i in df.index:
    rating = str(df.at[i,'all_reviews'])
    final = rating.split()[1]
    df.at[i,'all_reviews'] = final
'''
'''
df = encode(df,'tags',350)
df = encode(df,'publisher',1565)
df = encode(df,'developer',2273)
df.drop('tags',axis = 1, inplace=True)
df.drop('publisher',axis = 1, inplace=True)
df.drop('developer',axis = 1,inplace=True)
print(df.shape)
df.drop('name',axis=1,inplace=True)
df.drop('url',inplace=True,axis=1)
'''



#df.to_csv('dataset/merged2.csv',index=False)
