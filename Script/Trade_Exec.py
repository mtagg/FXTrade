###all functions required to interact and trade with the OandaPy platform
import CONFIG
import oandapy as opy
import pandas as pd
import os.path
import json
from datetime import date
from datetime import datetime

##initialize REST API
op = opy.APIv20(environment="practice", access_token=CONFIG.access_token, timeout=3)


def tradeProfile(Long):
    currPrice = op.pricing.get_pricing(
        account_id=CONFIG.account_id, instruments=CONFIG.INSTRUMENT
    ).as_dict()
    if Long == True:
        currAsk = float(
            list((list(list(currPrice.values())[1][0].values()))[3][0].values())[0]
        )
        # units = str(CONFIG.LOT_SIZE)
        units = 100
        bet = "Long"
        tp = round(currAsk + CONFIG.TAKE_PROFIT, 5)

    elif Long == False:
        currBid = float(
            list((list(list(currPrice.values())[1][0].values()))[2][0].values())[0]
        )
        # units = str(-CONFIG.LOT_SIZE)
        units = -100
        bet = "Short"
        tp = round(currBid - CONFIG.TAKE_PROFIT, 5)
    else:
        print("Unexpected value for Long/Short")
        return None, None

    takeProfit = {"price": (str(tp)), "timeInForce": "GTC"}
    stopLoss = {"distance": str(CONFIG.STOP_LOSS), "timeInForce": "GTC"}
    order = {
        "units": str(units),
        "instrument": CONFIG.INSTRUMENT,
        "timeInForce": "FOK",
        "type": "MARKET",
        "positionFill": "DEFAULT",
        "takeProfitOnFill": takeProfit,
        "stopLossOnFill": stopLoss,
    }
    print("TAKE PROFIT SET AT: ", tp)
    ##### requesition of a trade from the Oanda trading platform
    op.orders.create_order(account_id=CONFIG.account_id, order=order)
    return bet


def purchase(Long, bid, ask, dSpent):
    try:
        bet = tradeProfile(Long)
        dSpent += CONFIG.LOT_SIZE
        writeTransaction("Buy", bid, ask, bet)
        print("Order Request Completed")
    except:
        print("Error Requesting Order")
    return dSpent


def inTrade(dGain, transID):
    ########need to update and return all daily gain, spent and recieved values!!!!

    openP = (op.positions.get_open_positions(account_id=CONFIG.account_id)).as_dict()
    if len(list(openP.values())[0]) != 0:  ##meaning there is a current order
        transID = int(list(openP.values())[1])
        return True, dGain, transID
    elif transID == None:
        return False, dGain, transID
    else:
        # Fetch info about last trade
        print("CURRENT TRANSID :", transID)
        try:
            tran = (
                op.trades.get_trade_details(
                    account_id=CONFIG.account_id, trade_id=transID
                )
            ).as_dict()
            buy_ask = float(list(list(tran.values())[0].values())[2])
            sell_bid = float(list(list(tran.values())[0].values())[13])
            dGain += float(list(list(tran.values())[0].values())[8])
            writeTransaction("Sold", sell_bid, buy_ask, "N/A")
            transID = None
            return False, dGain, transID
        except:
            print("Failed to check last trade's details")
            print("Returning inTrade==False")
            return False, dGain, transID


def writeTransaction(buySold, bid, ask, bet):

    ##writes to transaction log in CONFIG.FILE_PATH destination
    try:
        fileName = os.path.join(
            CONFIG.FILE_PATH, str(date.today()) + "_Transactions_Log.json"
        )

        with open(fileName, "a") as FILE:
            log_item = {
                "date-time": str(datetime.now()),
                "Action": buySold,
                "Bet": bet,
                "Quantity": "$" + str(CONFIG.LOT_SIZE),
                "Bid Price": "$" + str(bid),
                "Ask Price": "$" + str(ask),
            }
            json.dump(log_item, FILE, indent=4)

        print("Action: " + buySold)
        print("Quantity: $" + str(CONFIG.LOT_SIZE))
        print("Bet: " + bet + "\n")
        print("Transaction Recorded")

    except:
        print("\nFailed to Record the Transaction")
