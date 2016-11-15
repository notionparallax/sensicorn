from pymongo import MongoClient
from scipy.misc import imread
from StringIO import StringIO
import datetime
import dateutil.parser
import json
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import pandas as pd
import pymongo
import pytz
import requests
import signal
import sys
import time



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
        print "made",fileName
    if forReal:
        return os.system(command)

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


def getSampleWalkData(url):
    firstRefTry = getDFfromCSVURL(url, columnNames=["stickerID","xstickerID","detectionType","xID","timeStamp"])
    return firstRefTry.drop(["xstickerID","detectionType","xID"], 1)

def getTrainingWalkData(trainingWalkURLs, stickerLocations):
    trainingWalks = []
    for i, twURL in enumerate(trainingWalkURLs):
        thisData = getSampleWalkData(twURL)
        richStickerData = thisData.merge(stickerLocations,on="stickerID")
        richStickerData['time'] = richStickerData.apply(lambda x: sydTimeToUTC(dateutil.parser.parse(x.timeStamp, dayfirst=True)) , axis=1)
    #     richStickerData['sydtime'] = richStickerData.apply(lambda x: dateutil.parser.parse(x.timeStamp, dayfirst=True) , axis=1)
        richStickerData = richStickerData.drop(["timeStamp"], 1)
        richStickerData = richStickerData.sort_values("time", ascending=1)

        print "{}: {} TO {} ({}) {} rows".format(i,richStickerData.time.min(),
                                     richStickerData.time.max(),
                                     richStickerData.time.max() - richStickerData.time.min(),
                                     richStickerData.shape[0])

        trainingWalks.append(richStickerData)
    return trainingWalks

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

def robustRequest(request, headers, tries=10, timeoutSeconds=20):
        response = False
        with timeout(seconds=timeoutSeconds):
            for i in range(tries):
                if not response:
                    try:
                        response = requests.request("GET", request, headers=headers)
                        return response
                    except:
                        if i == tries-1:
                            print "{}\nfailed {} times".format(request, i+1), sys.exc_info()[1]
                            return False

def nSecondWindows(stickerRecordingsRow, baseStationData, personID=304, chunkLength=5.0, chatty=True):
    try:
        startTime = datetime.datetime.now()

        row = stickerRecordingsRow
        halfWindow = datetime.timedelta(seconds=chunkLength/2.0)
        ws = row.time - halfWindow
        we = row.time + halfWindow
        url = "http://ec2-52-65-111-92.ap-southeast-2.compute.amazonaws.com:3000"
        headers = {'authorization': "Basic ",# + key,
                   'content-type':  "application/json",
                   'cache-control': "no-cache"}

        request = "{}/find?minor[]={}&windowstart={}&windowend={}".format(
            url, personID, ws.isoformat(), we.isoformat())

        windowDetectionsResponse = robustRequest(request, headers)

        if windowDetectionsResponse:
            responseJSON = json.loads(windowDetectionsResponse.text)[u'results'][0]
            if len(responseJSON)>0:
                responses = pd.DataFrame.from_dict(responseJSON)
                responses['temptime'] = responses.apply(lambda x: dateutil.parser.parse(x.time, dayfirst=True) , axis=1)
                responses = responses.drop(['time'], 1)
                responses = responses.rename(columns = {'temptime':'time'})
                responses = responses.sort_values("time", ascending=1)

                responses = pd.merge(responses,baseStationData,on=["agentId"])
                responses = responses.drop(["agentId"], 1)
                # rescale rssi between 0 and max in positive numbers. Bigger number means more powerful signal
                minPower = -100 #min(responses.rssi)
                responses['rssiAdj'] = responses.rssi - minPower

                if chatty:
                    print "index: {}\n{}\nstart: {}\ndetection: {}\nend: {}\ntook: {}\nresult rows: {}\n".format(
                        row.name,row, ws, row.time, we, datetime.datetime.now() - startTime, responses.shape[0])

                return responses
            else:
                return "no detections found, deal with this later"

        else:
            #the request returned false, so so will we
            return "detection request failed, deal with this later"
    except:
        print "OH FUCK"
        print sys.exc_info()
        print row
        return "Something seriously pooped its pants"


def timeSliced(fullRow, savePlace, contextDF, baseStationData, stickerLocations, personID=304):
    df = fullRow.detections

    fig, ax = plt.subplots()

    timeFormatString = "%H:%M:%S"
    title = "Detections for person {} around {}".format(personID, fullRow.time.strftime(timeFormatString))
    plt.title(title)

    #--- general vvv

    #put the image on the graph as an underlay
    img = imread("map.png")
    ax.imshow(img, zorder=0, extent=[-1300, 72000, -24000, 41000])
    #                                [left,  right, bottom, top  ]

    #put the baseStations on the map
    for index, row in baseStationData.iterrows():
        ax.text(row.x, row.y, row.agentName, fontsize=8)
    ax.scatter(baseStationData.x,baseStationData.y, marker='+')

    #Hide the axis numbers because they don't tell us much
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())

    #--- specific to this animation vvv

    #the sticker labels
    for index, row in contextDF.iterrows():
        ax.text(row.x, row.y, "{0:03d}".format(row.stickerID), fontsize=8)

    #sticker dots
    ax.scatter(contextDF.x, contextDF.y, zorder=20)
    ax.scatter(stickerLocations.x,stickerLocations.y,s=1,c="y")

    #the path
    ax.plot(contextDF.x, contextDF.y, alpha=0.7, linewidth=1, c="g", solid_capstyle='round')

    #--- specific to this frame vvv

    # Plot all the detections onto the map as pale circles
    ax.scatter(df.x, df.y, zorder=1, s=abs(df.rssiAdj)*100, alpha=0.2)

    #plot the current window's dot bigger
    ax.scatter(fullRow.x, fullRow.y, zorder=30, s=150, c="r")

    #--- clean up vvv
    print "saving to:", savePlace+title+".png"
    fig.savefig(savePlace+title+".png", bbox_inches='tight')
    fig.clf()
    plt.close()