# #Example that uses binary search
# def find_item(list, item):
#   #Returns True if the item is in the list, False if not.
#   if len(list) == 0:
#     return False

#   #Is the item in the center of the list?
#   middle = len(list)//2
#   if list[middle] == item:
#     return True

#   #Is the item in the first half of the list? 
#   if item in list[:middle]:
#     #Call the function with the first half of the list
#     return find_item(list[:middle], item)
#   else:
#     #Call the function with the second half of the list
#     return find_item(list[middle+1:], item)

#   return False

# #Do not edit below this line - This code helps check your work!
# list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

# print(find_item(list_of_names, "Alex")) # True
# print(find_item(list_of_names, "Andrew")) # False
# print(find_item(list_of_names, "Drew")) # True
# print(find_item(list_of_names, "Jared")) # False


# #Another example using 
# def binary_search(list, key):
#     #Returns the position of key in the list if found, -1 otherwise.

#     #List must be sorted:
#     list.sort()
#     left = 0
#     right = len(list) - 1

#     while left <= right:
#         middle = (left + right) // 2

#         if list[middle] == key:
#             return middle
#         if list[middle] > key:
#             print("Checking the left side")
#             right = middle - 1
#         if list[middle] < key:
#             left = middle + 1
#             print("Checking the right side")
#     return -1 

# print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
# """Should print 2 debug lines and the return value:
# Checking the left side
# Checking the left side
# 0
# """

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# """Should print no debug lines, as it's located immediately:
# 4
# """

# print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
# """Should print 3 debug lines and the return value:
# Checking the right side
# Checking the left side
# Checking the right side
# 6
# """

# print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
# """Should print 3 debug lines and the return value:
# Checking the right side
# Checking the right side
# Checking the right side
# 9
# """

# print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
# """Should print 4 debug lines and the "not found" value of -1:
# Checking the right side
# Checking the right side
# Checking the right side
# Checking the right side
# -1
# """


##Using the futures module to assign functions to threads.
# from concurrent import futures

# executor = futures.ThreadPoolExecutor() #Defines an executor - this will distribute work among different workers

# executor.submit(myFunction) #Submits a funtion to the executor - all functions submitted will be distributed among different workers and ran in parallel.

# print("Waiting for all threads to finish")
# executor.shutdown() #Shuts down the executor. The executor only shuts down when ALL threads have finished running through their assigned functions.


# executor = futures.ProcessPoolExecutor() #Here we say we want to use processes instead of threads for the parallel operations. 