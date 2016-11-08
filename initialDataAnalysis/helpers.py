import pymongo
from pymongo import MongoClient
import datetime
import dateutil.parser
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
from scipy.misc import imread
from StringIO import StringIO
import math
import pytz



SHOW_TESTS = False

def getDFfromCSVURL(url,columnNames=False):
    r = requests.get(url)
    data = r.content
    if columnNames:
        return pd.read_csv(StringIO(data),header=0,names=columnNames)
    else:
        return pd.read_csv(StringIO(data))

if SHOW_TESTS:
    print getDFfromCSVURL("https://docs.google.com/spreadsheets/d/1sijQZR2iFLo2FS_3r5gbsuAkaglRz557LWjdLxnPkpE/pub?gid=0&single=true&output=csv").head(3)
    print getDFfromCSVURL("https://docs.google.com/spreadsheets/d/1uE_tUItRANypaWxCmZeXWsgFZq_JDG626v4Gg2UQfKg/pub?gid=952022876&single=true&output=csv",
                             columnNames=["a","b","c","d","e"]).head(3)



def timeStats(df, showprint=True, actuallyReturn=True):
    #This gives us an idea of the time domain that the data we have is interested in.
    if showprint or actuallyReturn:
        minT = df.time.min()
        maxT = df.time.max()
        rangeT = maxT-minT
    else:
        print "are you mental, why are you calling this with everything turned off?"
    if showprint:
        print minT,   "First Recording in this set"
        print maxT,   "Last Recording in this set"
        print rangeT, "Range covered"
    if actuallyReturn:
        return (minT,maxT,rangeT)

if False:#SHOW_TESTS:
    timeStats(bigdf,showprint=False, actuallyReturn=False)
    print
    timeStats(bigdf, actuallyReturn=False)
    print timeStats(bigdf, showprint=False), "\n"
    timeStats(bigdf)


def timeCropDf(df, startTime, windowLength):
    if type(startTime) is str:
        startTime = dateutil.parser.parse(startTime)
    delta = datetime.timedelta(seconds=windowLength)
    endTime = startTime + delta
    return df[(df.time > startTime) &
              (df.time < endTime)]

if SHOW_TESTS:
    print "no tests written yet"


def makeGif(fromPath, fileName, stepSize="", forReal=True, chatty=True):
    #send a system command to make this into a gif. See https://community.linuxmint.com/tutorial/view/1118
    command="convert -delay 20 -loop 0 {} {}{}.gif".format(fromPath, fileName, stepSize)
    if chatty:
        print command
    if forReal:
        os.system(command)

if SHOW_TESTS:
    print "no tests written yet"


# In[9]:

def clearFolder(path):
    mydir = os.getcwd() + path
    map( os.unlink, [os.path.join( mydir,f) for f in os.listdir(mydir)] )

if SHOW_TESTS:
    print "no tests written yet"


# In[10]:

def sydTimeToUTC(naiveTime):
    ausSyd = pytz.timezone ("Australia/Sydney")
    local_dt = ausSyd.localize(naiveTime)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt

if SHOW_TESTS:
    for z in pytz.country_timezones['au']:
        print z
    print              datetime.datetime(2016,10,17,11,21,32) , "Australia/Sydney"
    print sydTimeToUTC(datetime.datetime(2016,10,17,11,21,32)), "UTC"

