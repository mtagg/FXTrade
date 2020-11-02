##alpha_vantage API Functions and library to obtain data
import os.path
import CONFIG  
import json    
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.techindicators import TechIndicators
from datetime import datetime
from datetime import date

FX = ForeignExchange(key=CONFIG.MY_ALPHA_KEY)    
ti = TechIndicators(key=CONFIG.MY_ALPHA_KEY)


def currentData(FROM,TO):
     ##current Exchange rate from alphavantage
     

     RATE, meta = FX.get_currency_exchange_rate(
                         from_currency=FROM,to_currency=TO)
     keys = list(RATE.keys())
     values = list(RATE.values())

     fileName = os.path.join(CONFIG.FILE_PATH, str(date.today())+"-CurrentRate.txt")
     with open(fileName,"a") as FILE:   
          FILE.write('\n')     
          FILE.write(str(datetime.now())+'\n')
          FILE.write((keys[0])+': '+(values[0]))
          FILE.write((keys[2])+': '+(values[2]))
          FILE.write((keys[4])+': '+(values[4]))
          FILE.write((keys[7])+': '+(values[7]))
          FILE.write((keys[8])+': '+(values[8]))
          FILE.write('\n')

     return keys, values

def recentData(FROM,TO,INTERVAL):
     
     Open  = []
     High  = []
     Low   = []
     Close = []

     ##fetch 100 most recent rates at INTERVAL seperation
     INTRA, meta = FX.get_currency_exchange_intraday(
                    from_symbol=FROM,to_symbol=TO,interval=INTERVAL,
                    outputsize='compact')  
     timeStamps = list(INTRA.keys())##(timestamp, open, high, low, close)
     Values = list(INTRA.values())##{open: xx, high: xx, low: xx, close: xx}   

     for dataPoint in Values:
          vals = list(map(float,dataPoint.values()))   
          Open.append (vals[0])
          High.append (vals[1]) 
          Low.append  (vals[2])
          Close.append(vals[3])


     fileName = os.path.join(CONFIG.FILE_PATH, str(date.today())+ "-IntraRate.txt")
     with open(fileName,"w") as FILE:
          FILE.write('100 Recent Values at 30min Intervals:\n\n\n')
          i = 0
          while i < len(INTRA):            
               json.dump(timeStamps[i],FILE)
               json.dump(Values[i],FILE)
               FILE.write('\n')
               i += 1

     return Open, High, Low, Close

def movingAverages(FROM, TO, int1,per1, int2,per2, int3,per3):
     ####Exponential Moving Averages
     EMA1, meta = ti.get_ema(FROM+TO, interval=int1, 
                              time_period=per1, series_type='close')
     ema1 = float((list((list(EMA1.values()))[0].values()))[0])    

     EMA2, meta = ti.get_ema(FROM+TO, interval=int2, 
                              time_period=per2, series_type='close')
     ema2 = float((list((list(EMA2.values()))[0].values()))[0])

     EMA3, meta = ti.get_ema(FROM+TO, interval=int3, 
                              time_period=per3, series_type='close')
     ema3 = float((list((list(EMA3.values()))[0].values()))[0])
     
     return ema1,ema2,ema3 
     