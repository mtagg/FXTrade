import CONFIG
import FXT_Logic as logic
import Trade_Algorithm as algo
import alphaV_API as alpha
import Trade_Exec as te
import time
import os.path
from datetime import date
from datetime import datetime

##Variables Setup:

SAFETYSTOP = False
count = 0     #for timing intermittently active functions
dailySpent = 0
dailyGain = 0

transID = None ##most recent transaction ID to track if there has been a sale or not
Long = None ## to track Bullish or Bearish Trends

#Candlestick intervals used in each average calculation
int1 = '1min'
int2 = '5min'
int3 = '15min'
int4 = '30min'
int5 = '60min'
int6 = 'daily'

#Numer of Candlesticks used in each average calculation
per1 = 5
per2 = 15
per3 = 30
per4 = 60
per5 = 90
per7 = 288

      ###################CTRL-C TO STOP LOOP IN TERMINAL####################

while dailyGain > CONFIG.DAILY_MAX_LOSS:


     if SAFETYSTOP == True:
          break

     ##request current data
     try:
          key, values = alpha.currentData(
                                        CONFIG.FROM, CONFIG.TO)
          
          ema1,ema2,ema3 = alpha.movingAverages( CONFIG.FROM,
                                        CONFIG.TO,int1,per1,int1,per3,int3,per3)
          currRATE = float(values[4])
          currBID  = float(values[7])
          currASK  = float(values[8])
     

          if count % 5 == 0:##every 5mins (5 counts @ 1 count per min)
               Open, High, Low, Close = alpha.recentData(CONFIG.FROM, CONFIG.TO, int3)
               highAvg,lowAvg,hi15,lo15,hi30,lo30,hi60,lo60,hiday,loday = logic.dataComp(
                                                                           Open,High,Low,Close)    
          
          dailySpent, dailyGain, Long, transID, SAFETYSTOP  = algo.tradeAlgo(Long, transID,
                                   currRATE, currBID, currASK, ema1, ema2, ema3,
                                        highAvg, lowAvg, hi15, lo15, hi30, lo30, hi60, lo60, 
                                                       hiday, loday, dailyGain, dailySpent)
          logic.printValues(key, values, dailyGain, 
                                   dailySpent, ema1, ema2, ema3)
          if SAFETYSTOP == True:
               break
     except Exception as e:
          print("Error Accessing API")
          print(e)
     count += 1
     time.sleep(60)



##Closing information##

print("Trading has been terminated")
fileName = os.path.join(CONFIG.FILE_PATH, str(date.today())+"_Transactions_Log.txt")
with open(fileName, 'a') as FILE:
     FILE.write("\n\n")
     FILE.write(str(datetime.now()))
     FILE.write('\nTrading has been terminated\n')
     FILE.write('TOTALS: \n')
     FILE.write('Daily Spent: '+str(dailySpent)+'\n')
     FILE.write('Daily Gain: '+str(dailyGain)+'\n')
     FILE.write('Safety Stop Status: '+str(SAFETYSTOP)+'\n')




