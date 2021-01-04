#test call to purchase...

import CONFIG
import pandas as pd
import oandapy as opy

op = opy.APIv20(environment='practice', 
                         access_token=CONFIG.access_token,
                                    timeout=3)
currPrice = op.pricing.get_pricing(account_id=CONFIG.account_id,
                                             instruments=CONFIG.INSTRUMENT).as_dict()
currBid = float(list((list(list(currPrice.values())[1][0].values()))[2][0].values())[0])
currAsk = float(list((list(list(currPrice.values())[1][0].values()))[3][0].values())[0])
print(currBid)
print(currAsk)
tp = (str(round(currAsk + CONFIG.TAKE_PROFIT,5)))
print(tp)



takeProfit = {
          "price" : tp,
               "timeInForce" : "GTC"
      }                
stopLoss = {
          "distance" : str(CONFIG.STOP_LOSS),
               "timeInForce" : "GTC"                 
     }
order = {
          "units": "100",      ##str(units),
               "instrument": CONFIG.INSTRUMENT,
                    "timeInForce": "FOK",
                         "type": "MARKET",
                              "positionFill": "DEFAULT", 
                                   "takeProfitOnFill" : takeProfit,
                                        "stopLossOnFill" : stopLoss
     }


print("requesting order")
try:
     op.orders.create_order(account_id=CONFIG.account_id, order=order)
     print("request successful")
except:
     print('request unsuccessful')
