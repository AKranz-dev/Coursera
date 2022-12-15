# #Write a python program to find URLs in a given text
# import re
# def url_Present(text):
#         pattern = r"[A-Za-z]*:*[\/]*www.?[A-Za-z0-9-\.]*\/?[A-Za-z0-9-\/]*"
#         result = re.search(pattern, text)
#         return result

# print(url_Present("My favorite website is www.youtube.com!"))
# print(url_Present("Look out for http://www.TumBlr2.net!"))
# print(url_Present("Every heard of www.google.net/ansi? Its the best!"))
# print(url_Present("http://www.google.com"))
# print(url_Present("http://www.google3.com/wargames/erc123/By-TheDoxesn/"))


# #Write a Python program that takes a string with some words. For two consecutive words in the said string, check whether the first word ends with a vowel and the next word begins with a vowel. 
# #If the program satisfy the said condition, return true other false. Only one space is allowed between the words.

# import re
# def vowel_Check(text):
#     pattern = r"([A-Za-z0-9]\s[a-z])"
#     result = re.findall(pattern,text)
#     for match in result:
#             match = match.lower()
#             if match[0] in "aeiou":
#                 if match[2] in "aeiou":
#                     return "True"
#                 else:
#                     pass
#             else:
#                 pass
#     return "false"


     
# print(vowel_Check("These exercises can be used for practice.")) #-> True
# print(vowel_Check("Following exercises should be removed for practice.")) #-> False
# print(vowel_Check(")I use these stories in my classroom.")) #-> True
# print(vowel_Check("Are the last letter of a word and the first letter of the subsequent word b (as seperated by a space) both vowels?"))