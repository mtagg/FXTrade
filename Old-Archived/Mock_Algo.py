## Going Long ##

if ema1 > ema2:
     if ema2 > ema3:     
          if hi15 > hi60:
               Long = True
               if hi60 > hiday:
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True

               elif hi60 < hiday:
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True
                    Long = None

          elif hi15 < hi60:    
               if hi60 > hiday:
                    if Long == True:
                         try:
                              print("\nOrder requested!")
                              dSpent = te.purchase(Long, bid, ask, dSpent)
                         except:
                              print("Failed to execute order!")
                              print("\nSafety Stop has been activated\n")
                              return dSpent, dGain, Long, transID, True
                         Long = None
               elif hi60 < hiday: 
                    Long = None
     elif ema2 < ema3:
          if hi15 > hi60:
               if hi60 > hiday:
                    Long = True
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True
               elif hi60 < hiday:
                    Long = None
                    pass

          elif hi15 < hi60:   
               if hi60 > hiday:
                    Long = True
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True
               elif hi60 < hiday:                   
                    Long = None
                    pass


## Going Short ##

elif ema1 < ema2:
     if ema2 < ema3:
          if lo15 < lo60: 
               Long = False  
               if lo60 > loday:
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True
               elif lo60 < loday:
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True    
          elif lo15 > lo60:
               if lo60 > loday:
                    pass
               elif lo60 < loday:
                    if Long == True:
                         try:
                              print("\nOrder requested!")
                              dSpent = te.purchase(Long, bid, ask, dSpent)
                         except:
                              print("Failed to execute order!")
                              print("\nSafety Stop has been activated\n")
                              return dSpent, dGain, Long, transID, True 

     elif ema2 > ema3:
          if lo15 > lo60:
               if lo60 > loday:
                    Long = None

               elif lo60 < loday:
                    Long = None

          elif lo15 < lo60:    
               if lo60 > loday:
                    Long = True

               elif lo60 < loday:
                    Long = False
                    try:
                         print("\nOrder requested!")
                         dSpent = te.purchase(Long, bid, ask, dSpent)
                    except:
                         print("Failed to execute order!")
                         print("\nSafety Stop has been activated\n")
                         return dSpent, dGain, Long, transID, True

else:
     Long = None
     return dSpent, dGain, Long, transID, False