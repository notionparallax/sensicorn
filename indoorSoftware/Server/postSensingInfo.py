#! /usr/bin/python

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# POST SENSING DATA TO WEB SERVER
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This script will read the sensing data genereated from the USB device and send the data via HTTP



# - - - - - - - - - - - - - - - - - - - -
# IMPORT LIBARIES
# - - - - - - - - - - - - - - - - - - - -

# Generic Python libaries
import time
import datetime
import random

# HTML
import requests
import json

# Operating system libaries
import sys
import io           # NOTE: IS NEEDED?
import os

# Compression
import gzip
import StringIO

# - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - -
# DEFINRE FUNCTIONS
# - - - - - - - - - - - - - - - - - - - -

# Retreives the RPi serial for uploading which is inserted as a value within the detections
def getRPiSerial():

    # Insert dummy data to test if it works
    cpuserial = "0000000000000000"

    try:
        # Opens the file which contains the RPi serial at "/proc/cpuinfo"
        rpiInformationFile = open('/proc/cpuinfo','r')
        
        # Goes through each line to find the serial value
        for fileLine in rpiInformationFile:
            if fileLine[0:6] == 'Serial':
                # Upon sucessful find, copy the characters
                cpuserial = fileLine[10:26]
        
        # Close connection once done
        rpiInformationFile.close()

    # If the file cannot be read
    except:
        cpuserial = "ERROR000000000"

    # Returns string of the RPi serial
    return cpuserial


# Check if the input value is a Float (decimal number)
def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


# Check if the input value is a integer (whole number)
def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

# - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - -
# DEFINE VARIABLES
# - - - - - - - - - - - - - - - - - - - -

# Server address and route
serverByURL = "http://ec2-52-65-111-92.ap-southeast-2.compute.amazonaws.com:3000"
serverPathing = "/upload/sensor"

# HTTP headers
httpHeaders = {"Content-Type":"application/octet-stream"}
httpAuthentification = ("understandingSpace", "knowledgeIsPower")

# Data read file
sensingDataFilePath = "senseData"

# Seeting temp variabls
filteredList = []
hasSent = False


# TESTING ON MAC, CANNOT GET SERIAL
# REMOVE THESE CONDITIONS AND KEEP LAST LINE
if True:
    rpiSerial = "000000000alexlee"
else:
    rpiserial = getRPiSerial()

# - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - -
# RUN ORDER
# - - - - - - - - - - - - - - - - - - - -

print "- - - - - - - - - - - - - - - - - - - - -"
rpiFile = open(sensingDataFilePath,'r')
for line in rpiFile:

    # Reset test variable
    good_detection = True

    # Remove white spaces + split
    list_values = line.split()

    # Checking mechanism
    if len(list_values) != 3:
        print "Error: Length of the list is not equal to 3, is incomplete or contains errors. Reported value:", len(list_values)
        good_detection == False
    else:
        if isFloat(list_values[0]) != True:
            print "Error: Temperature is not a float, is incomplete. Reported value:", list_values[0]
            good_detection == False

        if isFloat(list_values[1]) != True:
            print "Error: Volume is not a int, is incomplete. Reported value:", list_values[1]
            good_detection == False

        if isFloat(list_values[2]) != True:
            print "Error: Sound is not a int, is incomplete. Reported value:", list_values[2]
            good_detection == False

        # If sensor variables are all good, then formatting will proceed
        if good_detection:
            print "Sucess: Good recording found ~", list_values
            timeIsNow = datetime.datetime.now()
            compile_dictionary = {
                "rpi": rpiSerial,
                "temperature": float(list_values[0]),
                "volume": float(list_values[1]),
                "sound": float(list_values[2]),
                "time": (datetime.datetime.now()).isoformat()
            }
            filteredList.append(compile_dictionary)

        # If atleast one test failed, don't add to upload batch
        else:
            print "Fail: Detection has being filtered from the rest", list_values

# Close stream when finnished
rpiFile.close()

# Checks to see if any data has passed, will terminate on corrupt data.
if len(filteredList) == 0:
    print "No data has passed"
    sys.exit()

print "- - - - - - - - - - - - - - - - - - - - -"

print "Attempting to uploading " + str(len(filteredList)) + " sensor recordings."

# Create a File-Like-String to write compressed json data
out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode="w") as f:
    f.write(json.dumps(filteredList))



# Infinite loop which attempts to post the detection data
while hasSent == False:
    try:
        # HTTP post to insert into DB
        rZipped = requests.post(serverByURL + serverPathing, data=out.getvalue(), headers=httpHeaders, auth=httpAuthentification)
        # If the data could not be posted the attempt would stop here and proceed to "except"
        
        # Free the memory buffer, to prevent memory stackup
        out.close()
        # Stop infinite loop
        hasSent = True

    # On a failed attempt, the thread will rest then attempt another repost
    except:
        print "Failed trying again soon"
        time.sleep(300)

print "Sucessfully connected with server"
print rZipped.text



