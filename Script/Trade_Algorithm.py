import CONFIG
import Trade_Exec as te
import os.path

def tradeAlgo(Long, transID, rate, bid, ask, ema1, ema2, ema3,
                    highAvg, lowAvg, hi15, lo15, hi30, lo30,
                         hi60, lo60, hiday, loday, dGain, dSpent):

    # Check if in trade already, if spread is unreasonably large,
    # or if daily loss maximum has been reached
    spread = ask-bid
    inTrade, dGain, transID = te.inTrade(dGain, transID)

    if inTrade == True:
        print("Current Transaction ID: ", transID)
        return dSpent, dGain, Long, transID, False
    elif spread > CONFIG.MAX_SPREAD:
        return dSpent, dGain, Long, transID, False
    elif dGain <= CONFIG.DAILY_MAX_LOSS:
        return dSpent, dGain, Long, transID, True
    
    ## data algorithum calculations ##

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
                try:
                        print("\nOrder requested!")
                        dSpent = te.purchase(Long, bid, ask, dSpent)
                except:
                        print("Failed to execute order!")
                        print("\nSafety Stop has been activated\n")
                        return dSpent, dGain, Long, transID, True
                if lo60 > loday:
                    pass  
                elif lo60 < loday:
                    pass    
            elif lo15 > lo60:                
                if lo60 > loday:
                    pass
                elif lo60 < loday:
                    if Long == False:
                        try:
                            print("\nOrder requested!")
                            dSpent = te.purchase(Long, bid, ask, dSpent)
                        except:
                            print("Failed to execute order!")
                            print("\nSafety Stop has been activated\n")
                            return dSpent, dGain, Long, transID, True
                Long = None
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
    
    ## Default Position ##
    
    else:
        Long = None  

    return dSpent, dGain, Long, transID, False