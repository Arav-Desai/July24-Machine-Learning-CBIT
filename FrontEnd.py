import pandas as pd
from easygui import *
import joblib
import random

title="Car Price Predictor"
id=random.randint(40000000, 49999999)
cbs=[0,id]

#year
yr=integerbox("Production Year",title,upperbound=2024,lowerbound=1900 )
cbs.append(yr)

#category
categories=['Jeep' , 'Hatchback' , 'Sedan' , 'Microbus' , 'Goods wagon' , 'Universal' , 'Coupe' , 'Minivan' , 'Cabriolet' ,  'Limousine' , 'Pickup' ]
cate=choicebox("Which Category does your car:",title,choices=categories)
j=0
for i in categories:
    if i==cate :
        cbs.append(j)
    j=j+1


#leather interior
leather_interior=["No","Yes" ]
lt=choicebox("Does it have Leather Interior:",title,choices=leather_interior)
j=0
for i in leather_interior:
    if i==lt :
        cbs.append(j)
    j=j+1

#fuel type
fuel_type=['Hybrid', 'Petrol' ,'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
ft=choicebox("Which types of fuel it runs on:",title,choices=fuel_type)
j=0
for i in fuel_type:
    if i==ft :
        cbs.append(j)
    j=j+1

#engine volume
ev=enterbox("What is the volume of the engine:",title)
ev=float(ev)
cbs.append(ev)

#mileage
m=integerbox("Mileage of the car:",title,lowerbound=0,upperbound=1000000000)
cbs.append(m)

#cylliners
c=integerbox("How many cylinders does it contain:",title,lowerbound=0,upperbound=16)
cbs.append(c)

#gear box type
gear_box_type=['Automatic', 'Tiptronic', 'Variator', 'Manual']
gbt=choicebox("What type of gear box do you have",title,choices=gear_box_type)
j=0
for i in gear_box_type:
    if i==gbt :
        cbs.append(j)
    j=j+1

#drive wheels
drive_wheel=['4x4' ,'Front', 'Rear']
dw=choicebox("Drive wheels:",title,choices=drive_wheel)
j=0
for i in drive_wheel:
    if i==dw :
        cbs.append(j)
    j=j+1

#doors
doors=['4','1','>5']
d=choicebox("how many doors:",title,choices=doors)
j=0
for i in doors:
    if i==d :
        cbs.append(j)
    j=j+1

#wheel
wheel=['Left-hand drive', 'Right-hand drive']
w=choicebox("Which side streeing wheel:",title,choices=wheel)
j=0
for i in wheel:
    if i==w :
        cbs.append(j)
    j=j+1

#color
color=['Silver', 'Black' ,'White', 'Grey', 'Blue', 'Green' ,'Red' ,'Sky blue' ,'Orange','Yellow' ,'Brown', 'Golden' ,'Beige' ,'Carnelian red', 'Purple' ,'Pink']
col=choicebox("What is the color of your car:",title,choices=color)
j=0
for i in color:
    if i==col :
        cbs.append(j)
    j=j+1

#air bags
a=integerbox("How many airbags do you have:",title,lowerbound=0,upperbound=16)
cbs.append(a)

#opening model
model=joblib.load('CarPriceBackend.json')

parameters=['Unnamed: 0','ID', 'Prod. year','Category','Leather interior','Fuel type','Engine volume','Mileage','Cylinders','Gear box type','Drive wheels','Doors','Wheel','Color','Airbags']

input=pd.DataFrame([cbs],columns=parameters)

#predictions
pred=model.predict(input)

#message box output
title="Predicted Results"
output=msgbox(f"The Predicted Price of your Car is ${pred[0]}",title)
