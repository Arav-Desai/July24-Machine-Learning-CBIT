import pandas as pd
import numpy as np
import sklearn as skl
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import joblib as jl

xl=pd.read_excel('E:/CarPricePrediction/car price prediction.xlsx')
table=pd.DataFrame(xl)

table.Category=table.Category.map({'Jeep':0, 'Hatchback':1, 'Sedan':2, 'Microbus':3, 'Goods wagon':4, 'Universal':5, 'Coupe':6, 'Minivan':7, 'Cabriolet':8,  'Limousine':9, 'Pickup':10})
table["Fuel type"]=table["Fuel type"].map({'Hybrid':0, 'Petrol':1, 'Diesel':2, 'CNG':3, 'Plug-in Hybrid':4, 'LPG':5, 'Hydrogen':6})

table["Leather interior"]=table["Leather interior"].map({"Yes":1,"No":0})
#convert the turbo into 0
table["Engine volume"]=pd.to_numeric(table["Engine volume"],errors="coerce")
table["Engine volume"]=table["Engine volume"].fillna(0).astype(float)
#table['Engine volume'] = table['Engine volume'].apply(lambda x: float(x.replace(' Turbo', '').replace('km', '').strip()) if isinstance(x, str) and 'Turbo' in x else x)
#converting like engine volume
table["Mileage"]=table["Mileage"].str.replace('km','').astype(int)

table["Gear box type"]=table["Gear box type"].map({'Automatic':0, 'Tiptronic':1, 'Variator':2, 'Manual':3}).fillna(0)
table["Drive wheels"]=table["Drive wheels"].map({'4x4':0, 'Front':1, 'Rear':2})
table.Doors=table.Doors.map({4:4,1:1,'>5':5 }).fillna(0)
table.Wheel=table.Wheel.map({'Left-hand drive':0 , 'Right-hand drive':1}).fillna(0).astype(int)
table.Color=table.Color.map({'Silver':0, 'Black':1, 'White':2, 'Grey':3, 'Blue':4, 'Green':5, 'Red':6, 'Sky blue':7 , 'Orange':8, 'Yellow':9, 'Brown':10, 'Golden':11, 'Beige':12, 'Carnelian red':13, 'Purple':14, 'Pink':15}).fillna(0)

print(table.describe)
print(table.Mileage)
print(table["Engine volume"].tail())

#print(table["Engine Type"].tail())

x= table.drop(columns=["Manufacturer","Model","Price" ])
y= table.Price
print("x data type:",x.dtypes)
print("y data type:",y.dtypes)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size =0.30,random_state=42 )

lr=LinearRegression()
lr.fit(x_train ,y_train)

# Make predictions on the test set
Y_pred = lr.predict(x_test)
# model  performance
#r2 = r2_score(y_test , Y_pred)
#print(r2)

print(Y_pred)

#saving
jl.dump(lr,'CarPriceBackend.json' )