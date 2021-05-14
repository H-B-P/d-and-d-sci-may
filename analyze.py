import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("dset.csv")

df = df.fillna("N/A")
print(df)

def desp(s):
 return int(s.split("sp")[0])



winDf = df[df["Revenue From Selling Components"]!="N/A"]
lossDf = df[df["Revenue From Selling Components"]=="N/A"]

print(winDf)

winDf["Carver Bid"]=winDf["Carver Bid"].apply(desp)
winDf["Winning Bid"]=winDf["Winning Bid"].apply(desp)
winDf["Revenue From Selling Components"]=winDf["Revenue From Selling Components"].apply(desp)

lossDf["Carver Bid"]=lossDf["Carver Bid"].apply(desp)
lossDf["Winning Bid"]=lossDf["Winning Bid"].apply(desp)

print("all", "win", "loss")
print(len(df), len(winDf), len(lossDf))

print(df)

#Losses first

for unique in df["Species"].unique():
 sdf = lossDf[lossDf["Species"]==unique]
 print(unique, len(sdf))
 fig = go.Figure(data=go.Scatter(x=sdf["Days Since Death"], y=sdf["Winning Bid"], mode='markers'))
 fig.update_layout(title="Lost "+unique, xaxis_title="DSD", yaxis_title="WB")
 fig.update_traces(marker={"opacity":0.2})
 #fig.update_layout(xaxis={"range":[0,100]})
 fig.show()

#Then wins

for unique in df["Species"].unique():
 sdf = winDf[winDf["Species"]==unique]
 print(unique, len(sdf))
 fig = go.Figure(data=go.Scatter(x=sdf["Days Since Death"], y=sdf["Revenue From Selling Components"], mode='markers'))
 fig.update_layout(title="Win "+unique, xaxis_title="DSD", yaxis_title="RFSC")
 fig.update_traces(marker={"opacity":0.2})
 #fig.update_layout(xaxis={"range":[0,100]})
 fig.show()

#Check the averages aren't horribly misleading

for unique in df["Species"].unique():
 subDf = winDf[winDf["Species"]==unique]
 for days in range(12):
  subsubDf = subDf[subDf["Days Since Death"]==days]
  tot = float(sum(subsubDf["Revenue From Selling Components"]))
  if len(subsubDf)>0:
   print(unique, days, tot/len(subsubDf))
  else:
   print(unique, days, "IDK LOL")

  
  


