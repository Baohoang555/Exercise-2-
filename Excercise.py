    '''113. Write a  Python program that returns a string sorted alphabetically by the first character of a
    given string of words.
    Sample Data:
    ("Red Green Black White Pink") -> "Black Green Pink Red White"
    ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of
    sum said strings. the two")
    ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over
    quick the") '''

   
     sample_string = input("Enter your string,separated by comma: ").split()
     def get_first_char(string) :
         return string[0]
     def sorted_alphabetically(string) :
         return sorted(string, key=get_first_char)
     result = sorted_alphabetically(sample_string)
     print(result)
   
    '''112. Write a Python program to calculate the sum of two numbers given as strings. Return the
    result in the same string representation.
    Sample Data:
    ( "234242342341", "2432342342") -> "236674684683"
    ( "", "2432342342") -> False ( "1000", "0") -> "1000"
    ( "1000", "10") -> "1010'''
    
     number1 = int(input("Enter first number: "))
     number2 = int(input("Enter second number: "))
     str_num1 = str(number1)
     str_num2 = str(number2)
     if (str_num1 =="") or (str_num2 ==""):
         print("Error valid!")
     else:
         result = number1 + number2
      print("The sum of {} and {} is {}".format(str_num1, str_num2, result))
     111. Write a  Python program that takes a string and replaces all the characters with their
     respective numbers.
     Sample Data:
     110. Write a  Python program to insert space before every capital letter appears in a given word.
     Sample Data:
     ("PythonExercises") -> "Python Exercises"
     ("Python") -> "Python"
     ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
   
    def capital_string(string):
        result = ''
        for char in string:
            if char.isupper() and result:   If it's an uppercase letter and result is not empty
                result += ' '   Insert a space before the capital letter
            result += char   Add the current character
        return result
   
     Test cases
     sample_string = input("Enter your string: ")
     print(capital_string(sample_string))
    
    109. Write a Python program that counts the number of leap years within the range of years.
    Ranges of years should be accepted as strings.
    Sample Data:
    ("1981-1991") -> 2
    ("2000-2020") -> 6
  
   number1 = int(input("Enter first year: "))
   number2 = int(input("Enter second year: "))
   if number1 > number2:
       range_of_year = number1-number2
   else:
       range_of_year = number2-number1
   leap_year = range_of_year // 5
   if number1 %5 == 0 :
       leap_year += 1
   if number2 %5 == 0 :
       leap_year +=1
  
   str_leap_year = str(leap_year)
   print(leap_year)
  
  
   108. Write a  Python program that takes a string and returns  on both sides of each element,
   which are not vowels.
   Sample Data:
   ("Green" -> "-G--r-ee-n-"
   ("White") -> "-W--h-i-t-e"
   ("aeiou") -> "aeiou"
 
  sample_string = input("Enter your string:")
  def vowel_check(string):
      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      result = ''
      for char in string:
          if char not in vowels:
              result += '-' + char + ''
          else:
             result += char
      return result
  result = vowel_check(sample_string)
  print(result)
 107. Write a  Python program that takes two strings. Count the number of times each string
 contains the same three letters at the same index.
 Sample Data:
 ("Red RedGreen") -> 1
 ("Red White) -> 7
 ("Red White White Red") -


 def same_index(string1, string2):
     min_length = min(len(string1), len(string2))
     count = 0
     for i in range(min_length - 2):
         if string1[i: i + 3] == string2[i: i + 3]:
             count += 1
     return count

 sample_string1 = input("Enter your string 1: ")
 sample_string2 = input("Enter your string 2: ")
 result = same_index(sample_string1, sample_string2)
 print(result)
 106. Write a Python program to remove repeated consecutive characters and replace them with
 single letters and print a updated string.
 Sample Data:
 ("Red Green White") -> "Red Gren White"
 ("aabbbcdeffff") -> "abcdef"
 ("Yellowwooddoor") -> "Yelowodor"

 sample_string = input("Enter your string: ")


 def remove_duplicates(string):
     result = ""
     previous_char = ""

     for char in string:
         if char != previous_char:
             result += char
             previous_char = char

     return result



 result = remove_duplicates(sample_string)
 print(result)
 
 104. Write a  Python program that capitalizes the first letter and lowercases the remaining letters
 in a given string.
 Sample Data:
 ("Red Green WHITE") -> "Red Green White"
 ("w3resource") -> "W3resource"
 ("dow jones industrial average") -> "Dow Jones Industrial Average"

 sample_string = input("Enter a string: ")
 def capital_upper(string):
     first_letter = string[0].upper()
     return first_letter + string[1:].lower()
 print(capital_upper(sample_string))

 103. Write a  Python program to replace each character of a word of length five and more with a
 hash character ().
 Sample Output:
 Original string: Count the lowercase letters in the said list of words:
 Replace words (length five or more) with hash characters in the said string:
  the   in the said list of 
 Original string: Python - Remove punctuations from a string:
 Replace words (length five or more) with hash characters in the said string:
   -   from a 
 import string
 sample_string = input("Enter a string: ")
 def remove_punctuation(text):
     return ''.join(char for char in text if char not in string.punctuation)
 result = remove_punctuation(sample_string)
 print(result)
 101. Write a Python program to add two strings as if they were numbers (positive integer values).
 Return a message if the numbers are strings.
 Sample Output:
 42
 Error in input!
 Error in input!

 value = input("Nhập một giá trị: ")

 try:
     int_value = int(value)
     print(f"{int_value} là số nguyên.")
 except ValueError:
     print("Giá trị nhập vào là chuỗi, không phải số nguyên.")
 100. Write a  Python program to check whether any word in a given string contains duplicate
 characters or not. Return True or False.
 Sample Output:
 Original text:
 Filter out the factorials of the said list.
 Check whether any word in the said sting contains duplicate characrters or not!
 False
 Original text:
 Python Exercise.
 Check whether any word in the said sting contains duplicate characrters or not!
 False
 Original text:
 The wait is over.
 Check whether any word in the said sting contains duplicate characrters or not!
 True
 def has_duplicate_chars(word):

     return len(set(word)) < len(word)

 def contains_duplicate_word(text):

     words = text.split()
     return any(has_duplicate_chars(word) for word in words)

 text = input("Enter a string: ")

  In kết quả
 print("\nOriginal text:")
 print(text)
 print("Check whether any word in the said string contains duplicate characters or not!")
 print(contains_duplicate_word(text))

 99. Write a Python program to split a multi-line string into a list of lines.
 Sample Output:
 Original string: This
 is a
 multiline
 string.
  Split the said multiline string into a list of lines:
  ['This', 'is a', 'multiline', 'string.', ''
 sample_string = input("Enter a string: ").split()
 print(sample_string)
 98. Write a  Python program to decapitalize the first letter of a given string.
 Sample Output:
 java  Script
 python
 sample_string = input("Enter a string: ")
 result = sample_string[:1].lower() + sample_string[1:]
 print(result)
 97. Write a Python program to convert a given string to Snake case.
 Sample Output:
 java_script
 foo_bar
 foo_bar
 foo.bar
 foo_bar
 foo_bar
 foo_bar
 def to_snake_case(text):
     snake_case_text = ""

     for i, char in enumerate(text):
         if char.isupper() and i > 0 and text[i - 1] != " " and text[i - 1] != "_":
             snake_case_text += "_" + char.lower()   Add underscore before uppercase letters (except first letter)
         elif char == " " or char == "-":
             snake_case_text += "_"   Convert spaces and hyphens to underscores
         else:
             snake_case_text += char.lower()   Convert all characters to lowercase

     return snake_case_text


  Example usage
 input_text = input("Enter a string: ")
 print("Snake case:", to_snake_case(input_text))

 13. Write a  Python  script that takes input from the user and displays that input back in upper
 and lower cases.
 string = input("Enter a string: ")
 result1 = string.lower()
 result2 = string.upper()
 print(f"Upper case: {result2} and lower case: {result1}")

 14. Write a Python program that accepts a comma-separated sequence of words as input and
 prints the distinct words in sorted form (alphanumerically).
 Sample Words : red, white, black, red, green, black

 sample_string = input("Enter a string separated by a comma: ")
 words_list = [word.strip() for word in sample_string.split(",")]
 sorted_words = sorted(set(words_list))
 result = ", ".join(sorted_words)
  print(f"Sorted unique words: {result}")
 15. Write a  Python function to create an HTML string with tags around the word(s).
 Sample function and result :
 add_tags('i', 'Python') -> '<i>Python</i>'
 add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

 sample_string = input("Enter a string: ")
 tag = input("Enter a tag: ")
 print(f"add_tags('{tag}','{sample_string}') -> <{tag}>{sample_string}</{tag}>")

 16. Write a Python function to insert a string in the middle of a string.
 Sample function and result :
 insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
  insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
 sample_string1 = input("Enter a string: ")
 sample_string2 = input("Enter another string to insert in the middle of string: ")
 index_middlestr1 = int(len(sample_string1)/2)
 result = sample_string1[:index_middlestr1] + sample_string2 + sample_string1[index_middlestr1:]
 print(result)

 17. Write a Python function to get a string made of 4 copies of the last two characters of a
 specified string (length must be at least 2).
 Sample function and result :
 insert_end('Python') -> onononon
 insert_end('Exercises') -> eseseses

 sample_string = input("Enter a string: ")
 def char_last_two (string):
     last_two = string[-2:]
     return f"{last_two*4}"
 result = char_last_two(sample_string)
 print(result)
 18. Write a  Python function to get a string made of the first three characters of a specified string.
 If the length of the string is less than 3, return the original string.
 Sample function and result :
 first_three('ipy') -> ipy
 first_three(' python') -> pyt

 sample_string = input("Enter a string: ")
 def get_three_first(string):
     if len(string) <= 3:
         return string
     else:
         return string[:3]
 result = get_three_first(sample_string)
 print(result)
 19. Write a Python program to get the last part of a string before a specified character.
 https://www.w3resource.com/python-exercises
  https://www.w3resource.com/python
 sample_string = input("Enter a source of link: ")
 def remove_word(string):
     index_specified_char = string.find(".com/")
     if index_specified_char != -1:
         return string[index_specified_char+5:]
     else:
         return "Error source "

 result = remove_word(sample_string)
 print(result)
 20. Write a  Python function to reverse a string if its length is a multiple of 4.
 sample_string = input("Enter a string: ")
 def reverse(string):
     if len(string) %4 == 0:
         return string[::-1]
     else:
         return string
 result = reverse(sample_string)
 print(result)
 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
  uppercase characters in the first 4 characters.
 sample_string = input("Enter a string: ")


 def uppercase(string):
     first_four = string[:4]
     uppercase_count = sum(1 for char in first_four if char in string.upper())
     if uppercase_count >= 2:
         return string.upper()
     return string

 result = uppercase(sample_string)
 print(result)
 

 22.Write a  Python program to sort a string lexicographically.
 sample_string = input("Enter a string: ")
 words_list = [word.strip() for word in sample_string.split()]
 sorted_words = sorted(set(words_list))
 result = " ".join(sorted_words)
 print(result)
  23. Write a Python program to remove a newline in Python.
 sample_string = input("Enter a string: ")
 a = sample_string.replace("\n","")
 print(a)
 print(sample_string)
 24. Write a Python program to check whether a string starts with specified characters.
 def check_special_char(string):
     first_char = string[0]
     if not first_char.isalnum():

         return "k Co ki tu dac biet"
     else:
         return string
 sample_string = input("Please enter a string: ")
 print(check_special_char(sample_string))

  25. Write a Python program to create a Caesar encryption.
 Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
 code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
 type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
 number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
 by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
 private correspondence.
 esc ( bo qua )

 26. Write a  Python program to display formatted text (width=50) as output.
 import textwrap

 sample_string  = input("Enter a string: ")
 formatted_string = textwrap.fill(sample_string, width=50)
 print(formatted_string)

 27. Write a  Python program to remove existing indentation from all of the lines in a given text.

 sample_string = input("Enter a string: ").strip()
 print(sample_string)

 28. Write a Python program to add prefix text to all of the lines in a string.

 def add_prefix(text, prefix):
     lines = text.splitlines()
     prefixed_lines = [prefix + line for line in lines]
     return '\n'.join(prefixed_lines)

 sample_string = input("Enter a string: ")
 prefix = ">>"

 result = add_prefix(sample_string, prefix)
 print(result)

 29. Write a Python program to set the indentation of the first line.
 sample_string = input("Enter a string: ")
 print(f" {sample_string} ")

 30. Write a Python program to print the following numbers up to 2 decimal places.
 sample_num = float(input("Enter a number: "))
 print(f"{sample_num:.2f}")
 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.

 sample_num = float(input("Enter a number: "))
 print(f"{sample_num:.+2f}")
 32. Write a Python program to print the following positive and negative numbers with no
  decimal places.
 sample_num=float(input("Enter a number: "))
 print(f"{sample_num:+.0f}")
 33. Write a  Python program to print the following integers with zeros to the left of the specified
  width.
 sample_num = int(input("Enter a number: "))
 width= int(input("Enter a width: "))
 def zeros(value,widths):
        return str(value).zfill(widths)
 result = zeros(sample_num,width)
 print(result)


 35. Write a Python program to display a number with a comma separator.
 sample_value = input("Enter a list of numbers separated by a comma: ")
 sample_value = sample_value.split(',')
 print(sample_value)


 36. Write a Python program to format a number with a percentage.
 sample_value = float(input("Enter a number: "))
 print(f"{sample_value/100}%")

 37. Write a Python program to display a number in left, right, and center aligned with a width of
  10.
 num = int(input("Enter a number: "))

 print(f"Left aligned   : {num:<10}")
 print(f"Right aligned  : {num:>10}")
 print(f"Center aligned : {num:^10}")

 38. Write a Python program to count occurrences of a substring in a string.

 sample_string = input("Enter a string: ")
 substring = input("Enter a substring to count: ")

 count = sample_string.count(substring)
 print(f"The substring \"{substring}\" appears {count} times in the string.")


 39. Write a  Python program to reverse a string.
 sample_string  = input("Enter a string: ")
 print(sample_string[::-1])

 40. Write a Python program to reverse words in a string.

 sample_string = input("Enter a string: ")
 reversed_string = ' '.join(sample_string.split()[::-1])
 print(reversed_string)
 41. Write a  Python program to strip a set of characters from a string.

 sample_string = input("Enter a string: ")
 charater = input("Enter a character to remove from the string: ")

 resullt = ''.join(char for char in sample_string if char not in charater)
 print(resullt)

 42. Write a Python program to count repeated characters in a string.
 Sample string: 'thequickbrownfoxjumpsoverthelazydog'
 Expected output :
 o 4
 e 3
 u 2
 h 2
 r 2
 t 2

 sample_string = input("Enter a string: ")
 def count(string):
     char_frequency = {}
     for char in string:
         if char in char_frequency:
             char_frequency[char] += 1
         else:
             char_frequency[char] = 1
     return char_frequency
 result = count(sample_string)
 for char, freq in result.items():
     print(f"{char}: {freq}")


 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
 the volume of a cylinder.
 Sample output:
 The area of the rectangle is 1256.66cm2
 The volume of the cylinder is 1254.725cm3

 import math

 length = float(input("Enter the length of the rectangle: "))
 width = float(input("Enter the width of the rectangle: "))

 area_rectangle = length * width
 print(f"Area of the rectangle: {area_rectangle} m\u00b2")

 radius = float(input("Enter the radius of the cylinder: "))
 height = float(input("Enter the height of the cylinder: "))

 volume_cylinder = math.pi * (radius ** 2) * height
 print(f"Volume of the cylinder: {volume_cylinder:.2f} m\u00b3")

 44. Write a  Python program to print the index of a character in a string.
 Sample string: w3resource
 Expected output:
 Current character w position at 0
 Current character 3 position at 1
 Current character r position at 2 - - - - - - - - - - - - - - - - - - - - - - - - -
 Current character c position at 8
 Current character e position at 9

 sample_string = input("Enter a string: ")
 def index_character(string):
     for index,character in enumerate(string):
         print(f"Current character: {character} position at {index+1}")


 print(index_character(sample_string))

  45. Write a  Python program to check whether a string contains all letters of the alphabet.
 import string
 def contains_all_alphabets(s):
    s= s.lower()
    alphabet = set(string.ascii_lowercase)
    input_set = set(s)
    return alphabet.issubset(input_set)

 sample_string = input("Enter a string that contains all letters in alphabet: ")
 if contains_all_alphabets(sample_string):
     print("All letters present in the string are in the alphabet")
 else:
     print("All letters not in the string are in the alphabet")

 46. Write a Python program to convert a given string into a list of words.
 Sample Output:
 ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
 ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

 sample_string = input("Enter a string: ").split()
 print(sample_string)

 47. Write a  Python program to lowercase the first n characters in a string.
 sample_string =input("Enter a string")
 first_letter = sample_string[0].lower()
 result = first_letter + sample_string[1:]
 print(result)

 48. Write a Python program to swap commas and dots in a string.
 Sample string: "32.054,23"
 Expected Output: "32,054.23"

 sample_string = input("Enter a string: ")
 index_commas = sample_string.find(',')
 index_dots = sample_string.find('.')
 result = ""
 if index_commas != -1 and index_dots != -1 and index_commas < index_dots:
     result = sample_string.replace(',', '.')
 else:
     result = sample_string.replace('.', ',')
 print(result)
  49. Write a Python program to count and display vowels in text.
 sample = input("Enter a string: ").lower()
 def count_vowels(string):
     vowels = ['a', 'e', 'i', 'o', 'u']
     count = 0
     for char in string:
         if char in vowels:
             count += 1
     return count
 result = count_vowels(sample)

 print(result)

 50. Write a Python program to split a string on the last occurrence of the delimiter.


 def split_string(string,delimiter):
     position = string.rfind(delimiter)
     if position != -1:
         return string[:position],string[position +1:]
     else:
         return string,""


 sample_text = input("Enter a string: ")
 delimiter = input("Enter a delimiter: ")
 part1,part2 = split_string(sample_text,delimiter)
 print(f"Part before last delimeter: {part1}")
 print(f"Part before last delimeter: {part2}")

 51. Write a  Python program to find the first non-repeating character in a given string.
 sample_string = input("Enter a string: ").strip()
 def find_nonrepeat_words(string):
     counter = {}
     for char in string:
         if char in counter:
             counter[char] += 1
         else:
             counter[char] = 1
     return counter
 result = find_nonrepeat_words(sample_string)
 for key, value in result.items():
     if value ==1:
         print(f"{key}: {value}")

 52. Write a Python program to print all permutations with a given repetition number of characters
 of a given string.
 bỏ qua
 53. Write a Python program to find the first repeated character in a given string.
 sample_string = input("Enter a string: ").strip()
 def find_nonrepeat_words(string):
     counter = {}
     for char in string:
         if char in counter:
             counter[char] += 1
         else:
             counter[char] = 1
     return counter
 result = find_nonrepeat_words(sample_string)
 for key, value in result.items():
    if value >1:
        print(f"{key}: {value}")'

 54. Write a  Python program to find the first repeated character in a given string where the index
  of the first occurrence is smallest.
 sample_string = input("Enter a string: ")
 def count_character(string):
     count = {}
     for index,char in enumerate(string):
         if char in count:
             return char
         count[char] = index
     return None

 result = count_character(sample_string)
 print(result)

 55.Write a Python program to find the first repeated word in a given string.

 sample_string = input("Enter a string: ")
 def count_char(string):
     count = set()
     string = string.split()
     for char in string:
         if char in count:
             return char
         count.add(char)
     return None
 result = count_char(sample_string)
 print(result)

  56. Write a Python program to find the second most repeated word in a given string.
 def get_count(item):
     return item[1]


 def second_repeated_word(string):
     count = {}
     words = string.split()
     for word in words:
         if word in count:
             count[word] += 1
         else:
             count[word] = 1
     return count

     if len(count) < 2:
         return None
     sorted_words = sorted(count.items(), key=get_count, reverse=True)
     return sorted_words[1][0]


 sample_string = input("Enter a string: ")
 result = second_repeated_word(sample_string)
 print(result)

  57.Write a  Python program to remove spaces from a given string.
 sample_string = input("Enter a string: ").strip()
 print(sample_string)
  58. Write a Python program to move spaces to the front of a given string.
 sample_string = input("Enter a string: ")
 print(f" {sample_string}")

 59. Write a Python program to find the maximum number of characters in a given string.

 sample_string = input("Enter a string: ")
 def max_char_count(string):
     if not string:
         return None, 0
     max_char = max(set(string), key=string.count)
     return max_char, string.count(max_char)
 result = max_char_count(sample_string)
 print(result)
  60. Write a  Python program to capitalize the first and last letters of each word in a given string.
 sample_string = input("Enter a string: ")
 def capitalize(s):
     s = s.split()
     for word in s:
         first = word[0].upper()
         last = word[-1].upper()
         print(f"{first}{word[1:-1]}{last}")

 result = capitalize(sample_string)
 print(result)

  61. Write a Python program to remove duplicate characters from a given string
 sample_string = input("Enter a string: ")
 def remove_duplicate(string):
     count = set()
     result = ""
     for word in string:
         if word not in count:
             count.add(word)
             result += word
     return result

 r = remove_duplicate(sample_string)
 print(r)
 62. Write a Python program to compute the sum of the digits in a given string.
 def sum_digit(string):
   return  sum(int(char) for char in string if char.isdigit())
 sample_string = input("Enter a string: ")
 result = sum_digit(sample_string)
 print(result)
  Bai 1:
 x = input("Nhap chuoi cua ban: ")
 print(len(x))
  Bai 2: Write a Python program to count the number of characters (character frequency) in a string.
 x = "google.com"
 import string
 from dataclasses import replace
 from posixpath import split

 def char_frequency(string):
     char_fre={}
     for char in string:
         if char in string:
             char_fre[char] +=1
         else:
             char_fre[char]=1
     return char_fre

 result = char_frequency(x)
 print(result)
 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
 string. If the string length is less than 2, return the empty string instead.
 """sample_string = input("Enter your string: ")

 char = len(sample_string)
 if char<-2:
     print("")

 else:
     print(sample_string[0:2]+sample_string[-2:])"""


 4:Write a Python program to get a string from a given string where all occurrences of its first
 char have been changed to '$', except the first char itself.
 khong hieu de bai
 5: Write a Python program to get a single string from two given strings, separated by a space and
 swap the first two characters of each string

 """f_string = "123"
 s_string= "789"
 print(f_string[0:2]+s_string[0:2])"""

 """Bai 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
 the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
 less than 3, leave it unchanged."""
 """sample_string = input("Enter your example string: ")
 last_sen = sample_string[-3:]
 char = len(sample_string)
 def char_rep(string):
     if (len(string)>3):
         if(last_sen =="ing"):
             print(string.replace("ing","ly"))
         else:
             print(string+"ing")
     else:
         return string

 result = char_rep(sample_string)
 print(result)"""

 """7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
 string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
 resulting string."""

 '''sample_string = input("Enter your example string: ")

 """Sample String : 'The lyrics is not that poor!'
 'The lyrics is poor!'
 Expected Result : 'The lyrics is good!'
 'The lyrics is poor!' """

 def sen_replace(string):
     not_index = string.find("not")
     poor_index = string.find("poor")
     if not_index != -1 and poor_index != -1 and not_index < poor_index:
         string = string[:not_index] + 'good' + string[poor_index + 4:]
     return string
 result = sen_replace(sample_string)

 print(result)'''

 '''Write a  Python function that takes a list of words and return the longest word and the length
 of the longest one.
 sample_list = input("Enter a list of strings, separated by comma: ")
 sample_list = sample_list.split(",")
 print(sample_list)

 def longest_word(word_list):
     longest = ""
     for word in word_list:
         if len(word) > len(longest):
             longest = word
     return longest, len(longest)

 word, length = longest_word(sample_list)
 print(f"Longest word is: {word} and length: {length}")'''


 '''9. Write a Python program to remove the nth index character from a nonempty string.
 sample_string  = input("Enter your string: ")
 index_cha = int(input("Enter index character in string: "))

 if 0<=index_cha<len(sample_string):
     new_string= sample_string[:index_cha]+sample_string[index_cha+1:]
     print(new_string)
 else:
     print("Invalid Index")'''
 10: Write a  Python program to change a given string to a newly string where the first and last
 chars have been exchanged.
 '''
 sample_string = input("Enter your string: ")


 def exchanged_char(string):
     if len(string)<2:
         return string
     return string[-1] + string[1:-1] + string[0]

 result = exchanged_char(sample_string)
 print(result)'''

 '''11/Write a Python program to remove characters that have odd index values in a given string.
 sample_string = input("Enter your string: ")
 def remove_cha(string):
      for char in range(len(string)):
          if char % 2 == 0:
              result = ''.join([string[char]])
      return result
 result = remove_cha(sample_string)
 print(result)'''
 12Write a Python program to count the occurrences of each word in a given sentence.
 sample_string = input("Enter your string: ")

 def word_occurences(string):
     words = string.split()
     word_frequencies= {}
     for word in words:
         word = word.lower()
         if word in word_frequencies:
             word_frequencies[word] +=1
         else:
             word_frequencies[word] = 1
     return word_frequencies

 result = word_occurences(sample_string)
 print(result)
  13/ Write a  Python  script that takes input from the user and displays that input back in upper and lower cases.
 
  sample_string = input("Enter your string: ")
  print(sample_string)
  14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
 
  sample_string = input("Enter your string,separated by comma: ").split()
  print(sample_string)



