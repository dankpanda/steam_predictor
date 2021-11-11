import pandas as pd 
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv('dataset/merged3.csv')
x = df.iloc[:,1:]
y = df['all_reviews']

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.1,random_state=4)

regressor = XGBRegressor(eta=0.1,booster='gbtree',colsample_bytree= 0.6, gamma= 0, max_depth= 6, min_child_weight= 4,
                         subsample = 0.8, objective='reg:squarederror',tree_method='gpu_hist')

regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

from sklearn.metrics import r2_score,accuracy_score
print(r2_score(y_test,y_pred))








