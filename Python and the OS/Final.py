import re
from collections import OrderedDict

errorDict = {} #{"errorType" : errorCount}
per_user = {} #{"username" : {infoCount:, errorDict:}} - A dictionary of dictionaries


errorPattern = r"ERROR ([\w ]+[a-z]) \(([a-z.]+)\)" #Pattern to match error messages. Capture group 1 will capture the error type, and 2 will capture the username.
infoPattern = r"INFO[A-Za-z0-9\:\[\] \#]* \(([a-z.]+)\)" #Pattern to match info messages. Capture group 1 will capture the username.

#Now, parse through each log entry in the syslog.log file by iterating over the file.
with open ("~\syslog.log") as file:
    for row in file:
        result = re.search(errorPattern, row)
        
        if  result is not None:
            errorReason = result.group(1)
            errorUsername = result.group(2)
            if (errorReason in errorDict): #Checks if the error reason is in the error dictionary
                errorDict[errorReason] += 1 #If so, add 1 to the value of the error reason (which is the key)
            else:
                errorDict[errorReason] = 1 #If not, create an entry in the errors dictionary for the reason, and add 1 to the value
            if (errorUsername in per_user): #Checks if the username is in the per_user dictionary
                per_user[errorUsername]["ERROR"] +=1  #If so, add 1 to the number of errors for that user
            else:
                per_user[errorUsername] = {} #If not, create a dictionary of for the new user, initialize the info count, and add 1 to the error count
                per_user[errorUsername]["INFO"] = 0
                per_user[errorUsername]["ERROR"] = 1
        result = re.search(infoPattern, row)
        if re.search(infoPattern, row) is not None:
            infoUsername = result.group(1)
            if (infoUsername in per_user): #Checks if the username is in the user dictionary
                per_user[infoUsername]["INFO"] += 1 #If so, add 1 to the user's info count
            else:
                per_user[infoUsername] = {} #If not, create a dictionary for the new user, initialize the error count, and add 1 to the info count
                per_user[infoUsername]["INFO"] = 1
                per_user[infoUsername]["ERROR"] = 0
#Sort the errorDict by the most common errors to least common (dictionary sort method)
value_key_pairs = ((value, key) for (key,value) in errorDict.items())
sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
sortedErrorDict = {k: v for v, k in sorted_value_key_pairs}

#Sort the per_user by the username(alphabetical dictionary sort method)
sortedPer_User = OrderedDict(sorted(dict.items(per_user))) #This changes the object type to an OrderedDict - may be causing problems

#Write the data from the dictionaries, comma seperated, into the CSV files.
with open ("error_message.csv", "w") as errorCSV:
    errorCSV.write("Error,Count" + '\n')
    for key in sortedErrorDict:
        errorCSV.write(key + "," + str(sortedErrorDict[key]) + '\n')

with open ("user_statistics.csv", "w") as statsCSV:
    statsCSV.write("Username,INFO,ERROR" + '\n')
    for key in sortedPer_User:
        statsCSV.write(key + "," + str(sortedPer_User[key]["INFO"]) + "," + str(sortedPer_User[key]["ERROR"]) + '\n')
