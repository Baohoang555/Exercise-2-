# # Bai 1:
# #x = input("Nhap chuoi cua ban: ")
# #print(len(x))
# # Bai 2: Write a Python program to count the number of characters (character frequency) in a string.
# #x = "google.com"
# import string
# from dataclasses import replace
# from posixpath import split
#
# #def char_frequency(string):
#  #   char_fre={}
#   #  for char in string:
#    #     if char in string:
#     #        char_fre[char] +=1
#      #   else:
#       #      char_fre[char]=1
#     #return char_fre
#
# #result = char_frequency(x)
# #print(result)
# #3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# #string. If the string length is less than 2, return the empty string instead.
# """sample_string = input("Enter your string: ")
#
# char = len(sample_string)
# if char<-2:
#     print("")
#
# else:
#     print(sample_string[0:2]+sample_string[-2:])"""
#
#
# #4:Write a Python program to get a string from a given string where all occurrences of its first
# #char have been changed to '$', except the first char itself.
# #khong hieu de bai
# #5: Write a Python program to get a single string from two given strings, separated by a space and
# #swap the first two characters of each string
#
# """f_string = "123"
# s_string= "789"
# print(f_string[0:2]+s_string[0:2])"""
#
# """Bai 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged."""
# """sample_string = input("Enter your example string: ")
# last_sen = sample_string[-3:]
# char = len(sample_string)
# def char_rep(string):
#     if (len(string)>3):
#         if(last_sen =="ing"):
#             print(string.replace("ing","ly"))
#         else:
#             print(string+"ing")
#     else:
#         return string
#
# result = char_rep(sample_string)
# print(result)"""
#
# """7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
# string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string."""
#
# '''sample_string = input("Enter your example string: ")
#
# """Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!' """
#
# def sen_replace(string):
#     not_index = string.find("not")
#     poor_index = string.find("poor")
#     if not_index != -1 and poor_index != -1 and not_index < poor_index:
#         string = string[:not_index] + 'good' + string[poor_index + 4:]
#     return string
# result = sen_replace(sample_string)
#
# print(result)'''
#
# '''Write a  Python function that takes a list of words and return the longest word and the length
# of the longest one.
# sample_list = input("Enter a list of strings, separated by comma: ")
# sample_list = sample_list.split(",")
# print(sample_list)
#
# def longest_word(word_list):
#     longest = ""
#     for word in word_list:
#         if len(word) > len(longest):
#             longest = word
#     return longest, len(longest)
#
# word, length = longest_word(sample_list)
# print(f"Longest word is: {word} and length: {length}")'''
#
#
# '''9. Write a Python program to remove the nth index character from a nonempty string.
# sample_string  = input("Enter your string: ")
# index_cha = int(input("Enter index character in string: "))
#
# if 0<=index_cha<len(sample_string):
#     new_string= sample_string[:index_cha]+sample_string[index_cha+1:]
#     print(new_string)
# else:
#     print("Invalid Index")'''
# #10: Write a  Python program to change a given string to a newly string where the first and last
# #chars have been exchanged.
# '''
# sample_string = input("Enter your string: ")
#
#
# def exchanged_char(string):
#     if len(string)<2:
#         return string
#     return string[-1] + string[1:-1] + string[0]
#
# result = exchanged_char(sample_string)
# print(result)'''
#
# '''11/Write a Python program to remove characters that have odd index values in a given string.
# sample_string = input("Enter your string: ")
# def remove_cha(string):
#      for char in range(len(string)):
#          if char % 2 == 0:
#              result = ''.join([string[char]])
#      return result
# result = remove_cha(sample_string)
# print(result)'''
# #12Write a Python program to count the occurrences of each word in a given sentence.
# sample_string = input("Enter your string: ")
#
# def word_occurences(string):
#     words = string.split()
#     word_frequencies= {}
#     for word in words:
#         word = word.lower()
#         if word in word_frequencies:
#             word_frequencies[word] +=1
#         else:
#             word_frequencies[word] = 1
#     return word_frequencies
#
# result = word_occurences(sample_string)
# print(result)
# # 13/ Write a  Python  script that takes input from the user and displays that input back in upper and lower cases.
# #
# # sample_string = input("Enter your string: ")
# # print(sample_string)
# # #14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# #
# # sample_string = input("Enter your string,separated by comma: ").split()
# # print(sample_string)
#
