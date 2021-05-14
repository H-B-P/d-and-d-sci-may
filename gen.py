import numpy as np
import pandas as pd
import random
import math

def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op

def pseudo_poisson(tenths):
 ones=0
 for i in range(tenths):
  if roll_dX(10)==1:
   ones+=1
 return ones

def triangle_roll_dis(X):
 return min(roll_dX(X), roll_dX(X))

def triangle_roll_adv(X):
 return max(roll_dX(X), roll_dX(X))



def gen_days():
 return triangle_roll_dis(12)-1



def gen_yeti(days):
 return 72+roll_dX(6)-roll_NdX(days,6)

def gen_snow_serpent(days):
 return 20+roll_NdX(2,6)

def gen_winter_wolf(days):
 return 25-2*days+roll_NdX(4,6)



def alistair_bid(species, days):
 if species=="Yeti":
  return max(0, 55-days*6)
 elif species=="Snow Serpent":
  return max(0, 60-days*20)
 elif species=="Winter Wolf":
  return max(0, 50-days*12)

def betty_bid(species, days):
 if species=="Yeti":
  return 29+roll_dX(6)
 elif species=="Snow Serpent":
  return 9+roll_dX(8)
 elif species=="Winter Wolf":
  return 19+roll_dX(4)

def carver_bid(species, days):
 if species=="Yeti":
  return 32-2*days+roll_NdX(2,20)
 if species=="Snow Serpent":
  return 7+roll_NdX(2,10)
 if species=="Winter Wolf":
  return 31-3*days+roll_NdX(2,8)



vfuncLookup={"Yeti":gen_yeti, "Snow Serpent":gen_snow_serpent, "Winter Wolf":gen_winter_wolf}

dictForDf = {"Species":[], "Days Since Death":[], "Carver Bid":[], "Winning Bid":[], "Revenue From Selling Components":[]}

selector = ["Snow Serpent"]*5 + ["Winter Wolf"]*6 + ["Yeti"]*2

df=pd.DataFrame(dictForDf)

random.seed(0)

for i in range(1677):
 species = random.choice(selector)
 
 value_func = vfuncLookup[species]
 days = gen_days()
 value = value_func(days)
 
 BidA = alistair_bid(species,days)
 BidB = betty_bid(species, days)
 BidC = carver_bid(species, days)
 
 if BidC>max(BidA, BidB):
  newRow = {"Species": species, "Days Since Death":str(int(days)), "Carver Bid":str(int(BidC))+"sp", "Winning Bid": str(int(max(BidA, BidB, BidC)))+"sp", "Revenue From Selling Components":str(int(value))+"sp"}
 else:
  newRow = {"Species": species, "Days Since Death":str(int(days)), "Carver Bid":str(int(BidC))+"sp", "Winning Bid": str(int(max(BidA, BidB, BidC)))+"sp", "Revenue From Selling Components":"N/A"}
  
 df=df.append(newRow, ignore_index=True)

df=df[["Species", "Days Since Death", "Carver Bid", "Winning Bid", "Revenue From Selling Components"]]

print(df)

df.to_csv("dset.csv")




def desp(s):
 return int(s.split("sp")[0])

#consistency checking!
subset = df[df["Revenue From Selling Components"]!="N/A"]
print(sum(subset["Revenue From Selling Components"].apply(desp)), sum(subset["Carver Bid"].apply(desp)))

subsubset=subset[subset["Species"]=="Yeti"]
print(sum(subsubset["Revenue From Selling Components"].apply(desp)), sum(subsubset["Carver Bid"].apply(desp)))
subsubset=subset[subset["Species"]=="Snow Serpent"]
print(sum(subsubset["Revenue From Selling Components"].apply(desp)), sum(subsubset["Carver Bid"].apply(desp)))
subsubset=subset[subset["Species"]=="Winter Wolf"]
print(sum(subsubset["Revenue From Selling Components"].apply(desp)), sum(subsubset["Carver Bid"].apply(desp)))






random.seed(1234)

for i in range(13):
 species = random.choice(selector)
 value_func = vfuncLookup[species]
 days = gen_days()
 value = value_func(days)
 
 BidA = alistair_bid(species,days)
 BidB = betty_bid(species, days)
 BidC = carver_bid(species, days)
 
 print(str(i+1), species, days, value, max(BidA, BidB))
 
   
