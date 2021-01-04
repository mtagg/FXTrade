

def LongTermData(FROM,TO,readWrite):
     
     ##daily for the last 3+ months                     
     DAILY = FX.get_currency_exchange_daily(
                     from_symbol=FROM, to_symbol=TO,
                    outputsize='compact') 

          
     with open("IntraRate.txt","w") as FILE:
          json.dump(DAILY, FILE)

     ##monthly data to compare short frequency averages to
     
     MONTHLY = FX.get_currency_exchange_monthly(
                    from_symbol=FROM, to_symbol=TO,
                    outputsize='compact')

     with open("IntraRate.txt","w") as FILE:
          json.dump(MONTHLY, FILE)

##averages/values based on current data updates throughout the day
def movingAverages(prevCount, prev_rate_avg, prev_bid_avg, 
                         prev_ask_avg, rate, bid, ask):

     count = (prevCount + 1)
     rate_avg = (prev_rate_avg * prevCount + rate)  / count
     bid_avg  = (prev_bid_avg  * prevCount + bid)   / count
     ask_avg  = (prev_ask_avg  * prevCount + ask)   / count

     ### do i want to return max/min values instead? or a mixture?
     return (rate_avg, bid_avg, ask_avg)

def get_sma():

     ####Simple Moving Averages
     SMA1, meta = ti.get_sma(FROM+TO, interval=int1, 
                         time_period=20, series_type='close')
     ##i am sorry if anyone ever has to read this but i just had to xD
     sma1 = float((list((list(SMA1.values()))[0].values()))[0])
           ##sma1 == the most current calculated SMA value
           #     
     SMA2, meta = ti.get_sma(FROM+TO, interval=int2, 
                         time_period=20, series_type='close')
     sma2 = float((list((list(SMA2.values()))[0].values()))[0])

     SMA3, meta = ti.get_sma(FROM+TO, interval=int3, 
                         time_period=20, series_type='close')
     sma3 = float((list((list(SMA3.values()))[0].values()))[0])

     return sma1,sma2,sma3,ema1,ema2,ema3
 
 
###POTENTIAL VARIABLES:
###
###
###
###
#UNUSED VARIABLES
###
#rateAvg = 0  #50hr average
#bidAvg  = 0  #50hr average
#askAvg  = 0  #50hr average
#openAvg  = None #Avg from above lists
#closeAvg = None #Avg from above lists
#highAvg = None # average of high values from interval data
#lowAvg = None  # average of low  values from interval data

