from scrapDarkWeb import *
from databaseConnection import *
from flag import *

# Scrapping...

def getfunction(func):
        print("Scrapping in progress...")
        scrapRunning(func)
        isNodeBusy =True
        #Call each website scrap function here
        #try: scrapFuntion -> scrapSuccess(func) except: scrapFailure(func)

                                           

        # Add you try except (with elif condition here) just above this comment... 
        # Same as this Template: 
        
        # elif func=="{website name}":
        #         try:
        #                 print("{function name}Scrapping...please wait") 
        #                 {function name}
        #                 scrapSuccess(func)
        #         except:
        #                 print("{function name} not Scrapped!!")  
        #                 scrapFailed(func)       

        isNodeBusy=False      
