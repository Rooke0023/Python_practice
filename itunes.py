#CS50 Timestamp: 5:52:00

#Creating a web crawler in python that interacts with the itunes API to search for a song by the artist named Weezer.

import json
import requests
import sys

#Checking whether the user has input the name I, the programmer, want which is the name of the artist. If the input is less than 1 or more than two, the system will exit and won't execute any line of code after it.

if len(sys.argv) != 2:
    sys.exit("Error occurred. Don't give too many arguments. Limit it to only one.")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

#This code is meant to convert a JSON response from itunes API into a formatted JSON string with indentation for readability. The .json() is a method provided by the requests library that is performed on the object variable named response.

jsonFile = response.json()    #Created a varible that stores the https request in a json file
beautifyJsonFile = json.dumps(jsonFile, indent = 2)    #Converts the json file into python readable file
print(beautifyJsonFile)

    
    

