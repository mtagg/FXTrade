##FX_TRADE README.txt

          *************MAJOR PAIRS**************
[EUR_USD, 
     USD_JPY, 
          GBP_USD, 
               USD_CHF.]

Todo List:
"""""""""""""""""""""""""""""""""""""""""""""""

       ---email notifications when trading is cancelled
        ---periodic update emails??
         --- all try/except clauses implemented with error messages in main
          --- error message (+email)
    
""""""""""""""""""""""""""""""""""""""""""""""




Long Term indicator Research:
""""""""""""""""""""""""""""""""""""""""""""""""
     --- mean average convergance/divergance (MACD)
     --- stochastic oscillator
     --- LOOK INTO OTHER TECHNICAL INDICATORS ON av WEBSITE
     --- T3 triple exponential moving average? 

"""""""""""""""""""""""""""""""""""""""""""""""""""

           Long Term ToDo List:
          """""""""""""""""""""""""""""""""""""""
               ##lifetimetotalLoss = 0##possibly could be done through metatrader
               ##lifetimetotalGain = 0 ##possibly could be done through metatrader
               ##check beginning of day and if True: update
          
          """"""""""""""""""""""""""""""""""""""""
   
     


Functionality of this project:

     1. Periodically retrieve information from up to date 
     currency pair data source.

     2. Run data through a function algorithum to determine if 
     it should be acted on or not.

     3. If yes, access trading account and allocate funds to 
     purchase or to sell depending on outcome of algorithum.

     4. if no, no action taken, wait until next data fetch cycle.

     5. Output transactions into a text/json file titled with 
     the current date inside a folder labelled "transactions." 


Required Components:

     1. Main function to cycle fetch and action cycles periodically
     and provide timing data and variables to fuctions.

     2. Function to provide trading suggestions based on periodic data.
     This may consist of OR statements and considerations based on 
     current data, daily statistics, total loses, and gains etc.

     3. Output function to provide data for reader in the form of a
     .txt file which will log all transactions and account information 
     from time to time.

     4. Data fetching function, using internet connection, this will 
     fetch current trade data to send back to main for dispersment.

     5. Execute function to access trade account and perform 
     calculated actions.

     6. input into  Window's "Task Scheduler" during optimal times for
     trading the chosen currency.

     7. Error checking intra function to provide 
     feedback in case of a crash

     



Manual CURRENCY_EXCHANGE_RATE Rate Retrieval Instructions
 
API Parameters:
❚ Required: function
     The function of your choice. In this case, function=CURRENCY_EXCHANGE_RATE

❚ Required: from_currency
     The currency you would like to get the exchange rate for. 
     It can either be a physical currency or digital/crypto currency. 
     For example: from_currency=USD or from_currency=BTC.

❚ Required: to_currency
     The destination currency for the exchange rate. 
     It can either be a physical currency or digital/crypto currency. 
     For example: to_currency=USD or to_currency=BTC.

❚ Required: apikey

Example (for JSON output):

US Dollar to Japanese Yen:
https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=D3A51PW0J6G1LAJ0


