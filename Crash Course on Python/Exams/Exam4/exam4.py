# def format_address(address_string):
#     houseNumber = []
#     for char in address_string:
#                 if char.isnumeric():
#                     houseNumber.append(char)
#                 else:
#                     spaceIndex = address_string.index(char)
#                     break
    
#     houseNumber = "".join(houseNumber)
#     street = address_string[spaceIndex:]
#     street = street.strip()


#     return "house number {} on street named {}".format(houseNumber,street)

      
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# ===============================================================================

# def highlight_word(sentence, word):
# 	return(sentence.replace(word, word.upper()))

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# ===============================================================================

# def combine_lists(list1, list2):
#     attendance = []

#     for student in list2:
#         attendance.append(student)
#     for i in range (1, len(list1)):
#         attendance.append(list1[-i])
#     attendance.append(list1[0])

#     return attendance

	
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))


# ===============================================================================

# def squares(start, end):
# 	return [i*i for i in range (start, end+1)]

# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ===============================================================================


# def car_listing(car_prices):
#   result = ""
#   for car, price in car_prices.items():
#     result += "{} costs {} dollars".format(car, price)+ "\n"
#   return result
    

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


# ===============================================================================


# def count_letters(text):
#     result = {}
#     for char in count_letters:
#         if char != " ":
#             if char not in result:
#                 result[char] = 0
#             result[char] +=1
#     return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# ===============================================================================


# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   for letter in text:
#     if letter .isalpha():
#       letter = letter.lower()
#     # Check if the letter needs to be counted or not
#       if letter not in result:
#         result[letter] = 0
#     # Add or increment the value in the dictionary
#       result[letter] +=1
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


