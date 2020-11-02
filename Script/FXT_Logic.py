import CONFIG
from datetime import datetime
def printValues(key, values,
                    dailyGain, dailySpent,
                         ema1, ema2, ema3):
     ##print current currency values - dailygain/loss
     print()
     print(key[0],values[0])     ##from currency
     print(key[2],values[2])     ##to currency
     print(key[4],values[4])     ##exchange rate
     print(key[7],values[7])     ##bid price
     print(key[8],values[8])     ##ask price
     print('\n 5min EMA: ', ema1)
     print('30min EMA: ', ema2)
     print('7.5hr EMA: ', ema3)
     print('\nDaily Gain: $', dailyGain)
     print('Daily Spent: $', dailySpent)
     print('\n'+str(datetime.now())+ '\n')
     print("-----------------------------------------")
     


def dataComp(Open,High,Low,Close):

     ## compile data to be used in algo function

     ##lower indexed rates of the supplied lists are the most recent
     count = 100 ## len(supplied lists^^)
     hi15 = High[0]
     lo15 = Low[0]
     highAvg = 0
     lowAvg = 0
     i = 0
     while i < count:
          highAvg  += High[i]
          lowAvg   += Low[i]

          if i<2:
               hi30 = hi15
               lo30 = lo15

               if High[i]>hi15:
                    hi30 = High[i]
               if Low[i]<lo15:
                    lo30 = Low[i]

          elif i<4:
               hi60 = hi30
               lo60 = lo30

               if High[i]>hi30:
                    hi60 = High[i]
               if Low[i]<lo30:
                    lo60 = Low[i]

          else:
               hiday = hi60
               loday = lo60

               if High[i]>hi60:
                    hiday = High[i]
               if Low[i]<lo60:
                    loday = Low[i]
          i+=1

     highAvg  /= count
     lowAvg   /= count

     return highAvg,lowAvg,hi15,lo15,hi30,lo30,hi60,lo60,hiday,loday
