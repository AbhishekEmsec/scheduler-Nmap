from databaseConnection import *
import time
from bs4 import BeautifulSoup as bs
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime
import pymongo
from datetime import date
from itertools import zip_longest



from pymongo import MongoClient
def get_database():
   CONNECTION_STRING = "mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority"
   client = MongoClient(CONNECTION_STRING)
   return client['']
def scrapSuccess(func):
         collection.update_one({"name":func},{'$set':{"isUrgent":False,"status":"done","time":datetime.now()}})
def scrapFailed(func):
        collection.update_one({"name":func},{'$set':{"isUrgent":False,"status":"error","time":datetime.now()}})
def scrapRunning(func):
    collection.update_one({"name":func},{'$set':{"status":"running","time":datetime.now()}})


now=datetime.now()
CreatedDate =now.strftime("%d/%m/%y %H:%M:%S")



# #Add your function just above this comment...       
