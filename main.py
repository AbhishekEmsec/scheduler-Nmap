from flask import Flask
from databaseConnection import *
from bs4 import BeautifulSoup 
from mainScrapping import *
from datetime import date,datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flag import *

# Flask..
app = Flask(__name__)
def scrapping():
    print(datetime.now())
    if (isNodeBusy!=True):
        if collection.count_documents({'isUrgent':True})>0:
           
            print(f"No of urgent website :{collection.count_documents({'isUrgent':True})}")
            urgent1=collection.find({"isUrgent":True,"status":{"$ne":"running"}},{'_id':0,"name":1,"status":1,"isUrgent":1})
            print(urgent1[0]["name"])
            getfunction(urgent1[0]["name"]) 
      
        else:  
            d = datetime.today() - timedelta(hours=0, minutes=30)
            if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
                print(f"No of website whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
                urlList =collection.find({"status":{"$ne":"running"},"time":{"$lte":d}},{'_id':0,"name":1,"status":1,"isUrgent":1})
                print(urlList[0]["name"])            
                getfunction(urlList[0]["name"])    
            else:
                print("Every url Scrapped!!") 
    else:
        print("Node is Busy!!")

        
scrapping()
# Scheduler..
sched = BackgroundScheduler(daemon=True)
sched.add_job(scrapping,'interval',minutes=5)
sched.start()


@app.route('/')
def hello_world():
	return 'Hello Darkweb!!'


# main flask function
if __name__ == '__main__': 
    app.run()
