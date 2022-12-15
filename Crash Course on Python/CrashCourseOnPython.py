# name = "Brook"
# print("Hello " + name)

# print(4*5)
# print(100/2)
# print ((100/2)*50)

# #Outputs the data type of the input
# print(type("A"))
# print(type(1.5))

# length = 10
# width = 2
# area = length * width
# print(area)

# #Converts an int to a string
# base = 6
# height = 3
# area = (base*height)/2
# print("The area of the trianble is " + str(area))

# #Using Functions
# def greeting(name):
#     print ("Welcome, " + name)
# greeting("Austin")

# def greeting(name, department):
#     print ("Welcome, " + name)
#     print ("You are part of " + department)
# greeting("Austin", "IT")

# #Returing values
# def area_triangle(base, height):
#     return base*height/2
# area_a = area_triangle(5,4)
# area_b = area_triangle(7,3)
# sum = area_a + area_b
# print("The sum of both areas is: " + str(sum))

# def month_days(month,days):
#     print(month + " has " + str(days) + " days.")
# month_days("june",30)
# month_days("july",31)

# #Returning multiple values
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
# output = convert_seconds(500)
# print(output[1])

# #Comparisons
# print("cat" == "dog") #False
# print("cat" != "dog") #true
# print(10 > 2 and 50 > 25) #True
# print (10 < 2 or 2 > 1) #True
# print (not "cat" == "dog") #Prints opposite of comparison, prints True

# #Branching (if/else)
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     else:
#         print ("Username looks good!")
# hint_username("ab")

# #Using elif
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     elif len(username > 10):
#         print("Username too long")
#     else:
#         print ("Username looks good!")
# hint_username("ab")

# #While loops
# x = 0
# while x < 5:
#     print("Not there yet, x=" + str(x))
#     x = x+1
# print("x=" + str(x))

# #While loop in a function
# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x +=1
#     print("Done")
# attempts(10)

# #Using while not
# x = 0
# while not x==2:
#     print("X is not equal to 2")
#     x+=1

# #Using For loops
# for x in range(5):
#     print(x)

# #For loop to iterate through a list
# friends = ['Taylor', 'Alex', 'Shannon', 'Katie' ]
# for friend in friends:
#     print("Hi " + friend)

# product = 1
# for n in range(1,10):
#     product = product * n 
#     print(product)

# #Loop using custom incrementing
# for n in range(0,100,10):
#     print (n)

# #Using the end parameter in print removes the newline character
# for n in range(0,100,10):
#     print (n, end=" ")

# #Using the continue keyword to skip an iteration
# for n in range(0,100,10):
#     if n == 50:
#         continue
#     else:
#      print (n, end=" ")

# #Recursion = looping a function by calling itself until a condition is met
# def function(n):
#     if n > 10:  #base case
#         print ("Done!") 
#     else:
#         print(n)
#         function(n+1)   #recursive case
# function(1)

# #More recursion
# def sum_positive_numbers(n):
#     # The base case is n being smaller than 1
#     if n < 1:
#         return n
#     # The recursive case is adding this number to 
#     # the sum of the numbers smaller than this one.
#     return n + sum_positive_numbers(n-1)
# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# #Using string slicing to print a substring
# color = "orange"
# print(color[0:3])

# #More slicing!!
# fruit = "pineapple"
# print(fruit[:4]) #prints from nothing to 4 (first 4 characters)
# print(fruit[4:]) #prints from index 4 to the end of the string

# #using math to find a particular index
# color = "orange"
# print(color[0-4]) #computes 0-4 which is -3, and prints the -3 index which is n

# #You can concatenate slices together!
# fruit = "mangosteen"
# print(fruit[:5] + fruit[5:])

# #Correcting a string using slicing
# message = "A kong string with a silly typo"
# message = message[0:2] + "l" + message[3:]
# print(message)

# #Using a method to find the index of a character from a string
# pets = "Cats & Dogs"
# print(pets.index("C"))
# print(pets.index("&"))

# #Checking for substrings
# pets = "Cats & Dogs"
# print("Cats" in pets) #returns True
# print("Dragons" in pets) #returns False

# #Using format method to format strings
# name = "Manny"
# number = 8
# print("Hello {}, your lucky number is {}".format(name, number))

# #Using formatting expressions to alter the output of formatted text
# price = 7.50
# with_tax = 8.175
# print("Base price: ${:.2f} and price with tax: ${:.2f}".format(price, with_tax))

# #Using formatting to create some cool outputs
# def to_celsius(x):
#     return (x-32)*5/9
# for x in range(0,101,10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# #Using lists! 
# x = ["now", "we", "are", "cooking"]
# print(x)
# print(len(x)) #Outputs number of elements in a list
# print("are" in x)
# print(x[0])

# #Appending to lists
# fruits = ["pineapple", "banana", "apple", "melon"]
# fruits.append("kiwi")
# print(fruits)

# #Basic tuple
# myTuple = ("Grace", "M", "Hopper")

# #Iterating through a list
# animals = ["lion", "zebra", "dolphin", "monkey"]
# chars = 0
# for animal in animals: #for each animal in the list
#     chars += len(animal)  #Add the number of letters in the animal name
# print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# #Using enumerate to print the index and element value of a list
# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners): 
#     print(str(index) + "-" + person)

# #Iterating through a list of tuples, and doing stuff with the values in those tuples
# def full_emails(people):
#     result=[]
#     for email, name in people: #We know that people is made up of a list of tuples (first value being email, and second being name)
#         result.append("{} <{}>".format(name, email)) #Puts the name (second value provided to the function) in the first curly bracket, and puts the email (first value provided to the function) in the second curly brakcet
#     return result
# print(full_emails([("alex@example.com", "Alex Diego") , ("shay@example.com", "Shay Brandt")]))

# # Using list comprehension to more easily create a list
# myList = []
# for x in range(1,11):
#     myList.append(x*7)
# print(myList)
# #OR you can use list comprehension as follows
# myList = [x*7 for x in range(1,11)]
# print(myList)

# #Using list comprehension to print a list of the lengths of each item in the list
# languages = ["Python", "Perl", "ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# #Using list comprehension to create a list for every number in range 0 to 101 if that number % 3 is equal to 0.
# z=[x for x in range(0,101) if x % 3 == 0]
# print(z)

# #Crazy example using tuples and list comprehension
# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")] #list of tuples
#     # Iterate over each of the digits in octal
#     for digit in [int(n) for n in str(octal)]: #Create a list of integers (i.e. [7, 5, 5]) and iterate through each item
#         # Check for each of the permissions values
#         for value, letter in value_letters: #For each tuple in value_letters
#             if digit >= value: #if the digit is greater than the value of the current tuple (i.e. if 7 is greater than 4)
#                 result += letter #add the letter of the tuple to the result (i.e add r to the result)
#                 digit -= value #subtract the value from the digit (i.e 7-4 = 3)
#             else: #if the digit is NOT grater than the value of the current tuple
#                 result += "-"
#     return result
    
# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

# #Good tuple example
# def guest_list(guests): #list of tuples
# 	for name, age, job in guests: #for each tuple, assigning a name to each tuple value
# 		print("{} is {} years old and works as a {}".format(name, age, job))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# #Output should match:
# #Ken is 30 years old and works as Chef
# #Pat is 35 years old and works as Lawyer
# #Amanda is 25 years old and works as Engineer


# def bio_machine(bio_info):
#     userList = []
#     for name, job, age in bio_info:
#         newBio = "My name is {} and I am a {} year old {}.".format(name, age, job)
#         userList.append(newBio)
    
#     return(userList)

# myBios = [("Austin", "BodyBuilder", 25), ("Shannon", "Model", 25), ("Jerma", "E-clown", 30)] #A list of tuples
# print(bio_machine(myBios))

# #Using dictionaries!
# file_counts = {"jpg":10, "txt":14, "csv":2, "py": 23}
# print(file_counts)
# #Printing the value of a dictionary!
# print(file_counts["txt"])
# #Check if a value is in the dictionary!
# "jpg" in file_counts
# #Add a new element to the dictionary!
# file_counts["cfg"] = 8

# #Iterating through a dictionary - prints the keys
# file_counts = {"jpg":10, "txt":14, "csv":2, "py": 23}
# for extension in file_counts:
#     print(extension)

# #Iterating through the key/value pairs in a dictionary using the .items() method (returns a tuple)
# for ext, amount in file_counts.items():
#     print("There are {} files with the .{} extension".format(amount, ext))

# #Print out all keys and values in a dictionary
# print(file_counts.keys())
# print(file_counts.values())

# #Iterate through all value sin a dictionary!
# for value in file_counts.values():
#     print (value)

# #Using a dictionary to track how many unique letters are in a string
# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result

# print(count_letters("aaaa"))
# print(count_letters("tenant"))
# print(count_letters("Max should have let Checo pass in the Sao Paulo Brazillian Grand Prix"))

# #Nice example combining dictionaries and lists
# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for item, colorList in wardrobe.items():
#     for color in colorList:
#         print("{} {}".format(color,item))


# class Apple:  #Defining our class
#     color=""  #Giving our class attributes
#     flavor=""

# jonagold = Apple()  #Creating an instnace of our class - an object
# jonagold.color = "red" #Specifying the attributes of our object
# jonagold.flavor = "sweet"

# print(jonagold.color, jonagold.flavor)  #Printing the attributes of our object
# print(jonagold.color.upper()) #Using a string method on an attribute of our object (we can do this because the attribute is a string)

# #Creating our first method!
# class Piglet:
#     def speak(self):
#         print("oink oink")

# hamlet = Piglet()
# hamlet.speak()
    

# #Passing attributes of an object to a method
# class Piglet:
#     name = "piglet"
#     def speak(self):
#         print("Oink! I'm {}! Oink!".format(self.name))

# hamlet = Piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()

# petunia = Piglet()
# petunia.name = "Petunia"
# petunia.speak()

# #Returning values using a method
# class Piglet:
#     years = 0
#     def pig_years(self):
#         return self.years * 18

# piggy = Piglet()
# piggy.years = 2
# print(piggy.pig_years())


# # Constructor methods - setting object attributes on the object's creation!
# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor

# jonagold = Apple("red", "sweet")

# print(jonagold.color)
# print(jonagold.flavor)

# #Using the __str__ method to output useful information when we pass it to the print() function. Such as all values of all atributes!
# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#     def __str__(self):
#         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# jonagold = Apple("red", "sweet")
# print(jonagold)


# #Using docstrings to include useful information about our method
# class Person:
#   def __init__(self, name):
#     self.name = name
#   def greeting(self):
#     """Outputs a message with the name of the person"""
#     print("Hello! My name is {name}.".format(name=self.name)) 

# help(Person)


# #Using inheritance
# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor

# class Apple(Fruit): #Inherits from the Fruit class.
#     pass
# class Grape(Fruit): #Inherits from the Fruit class. 
#     pass

# granny_Smith = Apple("green", "tart") #Creates an instance of Apple, providing attribute values
# carnelion = Grape("purple", "sweet") #Creates an instance of Grape, providing attribute values

# print(granny_Smith.flavor)
# print(carnelion.color)

# #More ingeritance!
# class Animal: #Base Animal class
#     sound = ""
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

# class Piglet(Animal): #child class of animal
#     sound = "Oink!"

# hamlet = Piglet("Hamlet") #Object of Piglet. Passes "hamlet" to the constructor method to set the name. Inherits the sound attribute from the Piglet class.
# hamlet.speak()

# class Cow(Animal):
#     sound = "Moooo"

# milky = Cow("Milky")
# milky.speak()

# #Building a class with some cool methods - composition!
# class Repository:
#     def __init__(self):
#         self.packages = {}
#     def add_package(self, package):
#         self.packages[package.name] = package
#     def total_size(self):
#         result = 0
#         for package in self.packages.values():
#             result += package.size
#         return result


# #Using modules!
# import random
# print(random.randint(1,10)) #Using the randint method to generate a random number

# import datetime
# now = datetime.datetime.now() #Datetime module has a datetime class, which has a method called now
# print(now)
# print(now.year)
# print(now + datetime.timedelta(days = 28)) #Shows what day it will be in 28 days

# #Every variable initialized here
# #Filter by type and do stuff with each type
# #print(amount, animal, animals, base, carnelion, chars, color, colorList, __dict__, __doc__, ext, extension, Ellipsis)


