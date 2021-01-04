import CONFIG
import Trade_Exec as te
import os.path
from datetime import date
from datetime import datetime

currDate = date.today()
currTime = datetime.now() 
SAFETYSTOP = False
orderID = None
   ############################TEMPLATEE#####################################

def tradeAlgo(Long, rate, bid, ask, ema1, ema2, ema3,
                         highAvg, lowAvg, hi15, lo15, hi30, lo30, hi60, lo60, hiday, loday,
                                        dGain, dSpent):

     spread = ask-bid
     inTrade, dGain = ft.inTrade() ##confirms if in a trade or not before algorithm
     if inTrade == True:
          return dSpent, dGain, Long
     elif spread > CONFIG.MAX_SPREAD:
          return dSpent, dGain, Long
     elif dGain <= CONFIG.DAILY_MAX_LOSS:
          SAFETYSTOP = True
          return dSpent, dGain, Long

    
         ##data algorithum calculations

         """
     
     elif __________first condition___________:      
          try:  
          except:
     elif __________second condition___________:      
          try:  
          except:
     elif __________third condition___________:      
          try:  
          except:
     elif __________fourth condition___________:      
          try:  
          except:


               ................
     