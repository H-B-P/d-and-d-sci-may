import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

def get_ev_of_lot(species, days):
 if species=="Yeti":
  return 72+3.5-3.5*days
 if species=="Snow Serpent":
  return 20+3.5*2
 if species=="Winter Wolf":
  return 25-2*days+4*3.5

def alistair_bid(species, days):
 if species=="Yeti":
  return max(0, 55-days*6)
 elif species=="Snow Serpent":
  return max(0, 60-days*20)
 elif species=="Winter Wolf":
  return max(0, 50-days*12)

def betty_bids(species, days):
 if species=="Yeti":
  return [30,31,32,33,34,35]#29+roll_dX(6)
 elif species=="Snow Serpent":
  return [10,11,12,13,14,15,16,17]#9+roll_dX(8)
 elif species=="Winter Wolf":
  return [20,21,22,23]#19+roll_dX(4)

def get_profit_of_given_bid(bid, species, days):
 return get_ev_of_lot(species,days) - bid

def get_prob_of_given_bid(bid, species, days):
 aBid = alistair_bid(species, days)
 bBids = betty_bids(species,days)
 wins=0
 for bBid in bBids:
  if bid > max(bBid, aBid):
   wins+=1
 return float(wins)/float(len(bBids))

def get_ev_of_given_bid(bid, species, days):
 return get_profit_of_given_bid(bid, species, days)*get_prob_of_given_bid(bid,species,days)

def get_best_bid(species, days):
 aBid = alistair_bid(species, days)
 bBids = betty_bids(species, days)
 bestBid = 0
 EVtobeat = 0
 for bidToMatch in [aBid]+bBids:
  bid = bidToMatch+1
  EV = get_ev_of_given_bid(bid, species, days)
  if EV>EVtobeat:
   EVtoBeat=EV
   bestBid=bid
 return bestBid


for species in ["Yeti", "Snow Serpent", "Winter Wolf"]: 
 for days in range(12):
  print(species, days, get_best_bid(species, days))
