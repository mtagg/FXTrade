
##in [1]:

import configparser  
import oandapy as opy  
import pandas as pd
import numpy as np

config = configparser.ConfigParser()  
config.read('oanda.cfg')  

oanda = opy.APIv20(environment='practice',
                access_token=config['oanda']['access_token'])

                         ##do i need timeout?????????
                         # super().__init__(environment, access_token, timeout)
