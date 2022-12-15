# #Check CPU and Disk usage
# import shutil
# import psutil

# def check_disk_usage(disk):
#     du = shutil.disk_usage(disk)
#     free = du.free / du.total * 100
#     return free > 20

# def check_cpu_usage():
#     usage = psutil.cpu_percent(1)
#     return usage < 75

# if not check_disk_usage("/") or not check_cpu_usage():
#     print("ERROR!")
# else:
#     print("All good")


# #Absolute path to files: "G:\DevOps\Python\Projects\Coursera\Python and the OS\Files"
# import os
# os.chdir("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files")

# #Opening and reading a file
# file = open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt")
# print(file.readline())
# print(file.read())
# file.close()

# #Using with to automatically close the file for us
# with open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt") as file:
#     print(file.read())

# #Iterating through each line
# with open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt") as file:
#     for line in file:
#         print(line.upper())

# #Handling newline characters using the .strip() method
# with open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt") as file:
#     for line in file:
#         print(line.strip().upper())

# #Reading file lines into a list, and sorting
# file = open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt")
# lines = file.readlines()
# file.close
# lines.sort()
# print(lines)

# #Writing to a file
# with open("G:\DevOps\Python\Projects\Coursera\Python and the OS\Files\spider.txt", "w") as file:
#     file.write("It was a dark and stormy night")


# #Using the OS module (and the path submodule) to interact with files
# import os
# #os.remove("novel.txt") #Removes the given file
# print(os.path.exists("spider.txt")) #Checks if the given file path exists
# print(os.path.getsize("spider.txt")) #Gets size of given file

# print(os.path.getmtime("spider.txt")) #Gets time of the last edit to the given file - unix timestamp
# import datetime
# timestamp = os.path.getmtime("spider.txt")
# print(datetime.datetime.fromtimestamp(timestamp)) #Converts the Unix timestamp into readable datetime. The fromtimestamp is a method of the datetime class which is being called from the datetime module (datetime.datetime.fromtimestamp)
# print(datetime.datetime(2020, 1, 6, 7, 2, 3, 899999)) #Caliing the datetime class, passing in our own values for year, month, day, etc.

# print(os.path.abspath("spider.txt")) #Prints absolute path for a given file

# #Using the OS module to work with directories
# print(os.getcwd()) #Returns current working directory
# os.mkdir("MyNewDir") #Creates a directory
# os.chdir("MyNewDir") #Changes directory to the given path
# os.rmdir("MyNewDir")
# print(os.listdir())


# print(os.listdir("MyNewDir")) #Lists all items in the directory called "MyNewDir" which is present in our CWD

# myDir = "MyNewDir"
# for name in os.listdir(myDir): #For each file in the directory called "MyNewDir"
#     fullname = os.path.join(myDir, name) #Joining the directory name to the items listed in the directory - necessary for determining if the file is a directory
#     if os.path.isdir(fullname): #If this file is a directory...
#         print("{} is a directory".format(fullname))
#     else:
#         print("{} is a file".format(fullname))

# #Using the CSV module to unpack a CSV file
# import csv
# f = open("csv_file.txt") #Open the file
# csv_f = csv.reader(f) #Create your reader object to read the file, passing in the file
# for row in csv_f: #For every row in the CSV file,
#     name, phone, role = row #Parse the contents of the row into these variables
#     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()

# #Using CSV module to create and write to a csv file
# import csv
# hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]] #Created a list of lists
# with open("hosts.csv","w") as hosts_csv:
#     writer = csv.writer(hosts_csv) #Create your writer object, passing in the file name
#     writer.writerows(hosts) #Write the date

# #Using dictionaries to read from a csv file
# import csv
# with open("software.csv") as software: #Opens csv for reading
#     reader = csv.DictReader(software) #Creates the CSV Dictreader object
#     for row in reader:
#         print(("{} has {} users").format(row["name"], row["users"])) #Prints every row, corresponding the string format to the "key" of the data (column name set in the first row)


# #Using dictionaries to write to a CSV
# import csv
# users = [ {"name": "Nigel Mansel", "username": "n.mansel", "department": "IT"}, #we have a list of dictionaries
#           {"name": "Sebastian Vettel", "username": "s.vettel", "department": "HR"}] 
# keys = ["name", "username", "department"] #Created a list of collumn names, or "keys"
# with open ("by_department".csv, "w") as by_department: #Open our file for writing
#     writer = csv.DictWriter(by_department, fieldnames=keys) #Creating our writer - pasing in our target file for writing, and passing in our collumn list for the fieldnames
#     writer.writeheader() #writes
#     writer.wrtierows(users)


# #Using REGEX!
# import re
# result = re.search(r"aza", "plaza") #Specifying that we are searching against a raw string.
# print(result) #Prints the match. Shows us the index of where the match is. 
# result = re.search(r'aza', "bazaar")
# print(result)
# result = re.search(r"^x", "xenon") #Matches the beginning of the string, and then an x
# print(result)
# result = re.search(r"APP", "applebees", re.IGNORECASE) #Ignoring case
# print(result)

# #REGEX Character Classes
# import re
# print(re.search(r"[Pp]ython", "Python")) #Matches P or p
# print(re.search(r"[a-z]way", "The end og the highway")) #matches 'hway' in highway
# print(re.search(r"[a-z]way", "What a way to go")) #Doesnt match because there is a space before way

# print(re.search(r"[^a-zA-Z]", "cloud9")) #Matches the 9
# print(re.search(r"[^a-zA-Z]", "See ya")) #Matches the space
# print(re.search(r"[^a-zA-Z ]", "See ya!")) #Matches the !, now that we excluded spaces

# #REGEX OR operator and findall()
# import re
# print(re.search(r"cat|dog", "I like cats.")) #Matches cat
# print(re.search(r"cat|dog", "I like dogs.")) #Matches dog
# print(re.search(r"cat|dog", "I like cats and dogs.")) #Matches cats, we only get the first match
# print(re.findall(r"cat|dog", "I like cats and dogs.")) #Prints all matches! Returns a list of matches

# #Using the * and the | characters
# import re
# print(re.search(r"Py.*n", "Pygmalion")) #Matches a capital P, followed by a lowercase y, follwed by 1 or more of any character, followed by an n.
# print(re.search(r"Py.*n", "Python Programming")) #Matches ALL the way to the last n! You might expect it to stop at the first, but its greedy. 

# print(re.search(r"o+l+","goldfish")) #Matches ol
# print(re.search(r"o+l+","woolly")) #Matches ooll
# print(re.search(r"o+l+","woolly")) #Does not match 

# #Using the ? character - matches 0 or 1 of the preceeding token
# import re
# print(re.search(r"p?each", "To each their own")) #matches each (0 occurences of p)
# print(re.search(r"p?each", "I like peaches")) #matches peach (1 occurence of p)

# #Escaping characters in REGEX
# import re
# print(re.search(r"\.com","welcome")) #Does not match
# print(re.search(r"\.com","mydomain.com")) #matches.com

# print(re.search(r"\w*", "This is an example")) #Matches This - \w doesnt match spaces
# print(re.search(r"\w*", "This_is_an_example")) #Matches everything, as \w matches underscores, letters, and numbers


# #Using capture groups
# import re
# result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") #First capture group matches Lovelace, then a literal comma and a space, and then the second capture group captures ada
# print(result[0]) #Prints all matches
# print(result[1]) #Prints the first capture group
# print(result[2]) #Prints the first capture group
# print(result.groups()) #Returns a tuple of the matches. First element is the first match, and the second is the second match. We can select these with indexes.

# #REGEX repitition qualifiers and boundaries
# import re
# print(re.search(r"[a-zA-Z]{5}", " a ghost")) #Says that we want to match 5 instances in a row of the preceeding token (a-zA-Z) - matches ghost
# print(re.search(r"[a-zA-Z]{5}", "A scary ghost appeared")) #Matches scary, since its the first occurenace. use re.findall to return all results.
# print(re.findall(r"[a-zA-Z]{5}", "A scary ghost appeared")) #Matches scary, ghost, and appea
# print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #Matches scary, and ghost. Does not match partial parts of words.
# print(re.findall(r"[a-zA-Z]{5,10}", "I really like strawberries")) #Matches really (6 letters in a row) and strawberri (10 letters in a row)
# print(re.findall(r"[a-zA-Z]{5,}", "I really like strawberries")) #Matches really (>5 letters in a row) and strawberries (>5 letters in a row)
# print(re.findall(r"[a-zA-Z]{,5}", "I really like straberries")) #Matches between 0 and 5 consecitive occurences of your expression


# #Using REGEX with PIDs
# import re
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]:\s+([A-Z]*)"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return "{} ({})".format(result[1],result[2])
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]")) # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


# #REGEX re.split() and re.sub()
# import re
# print(re.split(r"[.?!]", "One sentence. Another one? And the last one!")) # Splits by either period, ? or !. Returns a list strings split by our pattern
# print(re.split(r"([.?!])", "One sentence. Another one? And the last one!")) # Use a capturing parenthesis to also return the elements that we are splitting by in our list of strings
# print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts85@gmail.com")) #Pattern looks for email addresses. Using re.sub to redact any email addresses.
# print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "lovelace, Ada")) #Combining capture groups with re.sub().


# #Good re.sub() example
# import re
# def convert_phone_number(phone):
#   result = re.sub(r"([a-z] )([0-9]{3})([- ]?)([0-9]{3})([- ]?)([0-9]{,5})", r"\1""("+r"\2"+")"+ " " + r"\4" + "-" + r"\6", phone)
#   return result
# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


# #Accepting user input
# name = input("Please enter your name: ")


# #Using the subprocess module to run shell commands
# import subprocess
# subprocess.run(["sleep", "2"])
# import subprocess
# result = subprocess.run(["host"], capture_output=True)
# print(result.returncode) #Prints the command's return code
# print(result.stdout) #Prints the STDOUT of the command (whatever the shell command returned)
# print(result.stdout.decode().split()) #Decodes the returned value to make it more readable, and splits it into a list
# result = subprocess.run(["rm", "my_file"], capture_output=True)
# print(result.returncode) #Shows return code of 1, the command failed
# print(result.stderr) #prints the error from the command


# # Using REGEX to filter through log files
# import sys
# import re

# logfile = sys.argv[1] #Takes the argument passed to the python script when it was invoked (likly passing in the absolute path of a log file)
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line: #Looks for any use of the CRON tool
#             continue
#         else:
#             pattern = r"USER \((\W+)\)$" #Looks for a username, captures the username in a capture group
#             result = re.search(pattern, line)
#             print(result[1]) #Prints the value of the capture group



# #Good example of parsing the syslog and extracting just the information we need
# import re
# def show_time_of_pid(line):
#   pattern = r"(\w{3}) ([0-9]{,2}) ([0-9]{2}:[0-9]{2}:[0-9]{2})[\w\s.=]*\[([0-9]{5})\]"
#   result = re.search(pattern, line)
#   return result[1] + " " + result[2] + " " + result[3] + " pid:" + result[4]

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440



# #Further improving our script to filter log files
# import re 

# logfile = sys.argv[1] #Takes the argument passed to the python script when it was invoked (likly passing in the absolute path of a log file)
# usernames = {}
# with open(logfile) as f:
#     for line in f:
#         if "CRON" not in line: #Looks for any use of the CRON tool
#             continue
#         else:
#             pattern = r"USER \((\W+)\)$" #Looks for a username, captures the username in a capture group
#             result = re.search(pattern, line)
#             if result is None: #If there is no REGEX match, abandon
#                 continue #Returns to the top of the loop
#             name = result[1] #name is the REGEX matched username
#             usernames[name] = usernames.get(name, 0) + 1 
#             print(result[1]) #Prints the value of the capture group

# usernames = {}
# name = "good_user"
# usernames[name] = usernames.get(name, 0) +1 #Using the get method on a dictionary to get the current value. If the key doesnt exist in the dictionary, it will be created and passed the 2nd parameter, 0. We are then adding +1 to the value if its found.



# #Writing unit tests!!!!!
# import unittest
# from rearrange import rearrange_name #Imports the rearrange_name function defined in our script called rearrange.py. rearrange.py MUST be in the same folder as our test script which references it.

# class TestRearrange(unittest.TestCase): #Here we are creating a class called TestRearrange - we are telling it to inherit functionality from the TestCase class, which is located in the unittest module.
#     def test_basic(self):
#         testcase = "Lovelace, Ada"
#         expected = "Ada Lovelace"
#         self.assertEqual(rearrange_name(testcase), expected) #Runs rearrange_name function (function we are testing) passing in our test case. assertEqual method checks if the given arguments match each other (testcase and expected)
    
#     def test_empty(self):  #This will produce an error, telling us that this test failed, and provides the error message.
#         testcase = ""
#         expected = ""
#         self.assertEqual(rearrange_name(testcase), expected)
    
#     def test_double_name(self): #Creating a test case for double names!
#         testcase = "Hopper, Grace M."
#         expected = "Grace M. Hopper"
#         self.assertEqual(rearrange_name(testcase), expected)

#     def test_one_name(self): #Creating a test case for a single name. Our app cannot handle this case, and it fails.
#         testcase = "Voltaire"
#         expected = "Voltaire"
#         self.assertEqual(rearrange_name(testcase), expected)

# unittest.main() #This function will run the test for us.


# #Raising errors and using Assert!
# def validate_user(username, minlen):
#     assert type(username) == str, "username must be a string"
#     if minlen < 1:
#         raise ValueError("minlen must tbe at least 1")
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return False
#     return True

# print(validate_user("edward", 0)) #Throws our ValueError
# print(validate_user(4, 1)) #Throws our assert error
