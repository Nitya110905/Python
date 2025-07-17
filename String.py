# s = "Python Programming"

# print(len(s)) 
# In Python, the length of a string is measured starting from 1, not 0.

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.center(30,"*"))
# print(s.count("m"))
# print(s.endswith("ng"))
# print(s.find("y"))
# print(s.isalnum())
# print(s.isalpha())
# print(s.replace("P","r"))
# print(s.swapcase())
# print(s.title())

# Mid of String
a = input("Enter Name : ")

if len(a) % 2 != 0:
    mid = len(a) // 2
    print("Middle Letter of", a, "is:", a[mid])
    print("Middle Letters:", a[mid-1], a[mid], a[mid+1])
else:
    print("String has even length; no single middle letter.")

word = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
word = word.lower()

if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
   #  The f in print refers to f-strings, introduced in Python 3.6. Used to embed variables directly in strings.
else:
    print(f"'{word}' is not a palindrome.")
   

#Slicing
# Slicing Syntax: text[start:end:step]

# s = "Python Programming"

# print(s[0:10:4])

# s = "Python is Best Language"

# print(len(s))
# print(s[3:21:3])
# print(s[:19:4])
# print(s[6::5])
# print(s[5:18:2])
# print(s[::1])
# print(s[:19:4])

# print(s[-17:-4:2])
# Start at index -17 equivalent to 7 (because 24 - 17 = 7)
# End before index -4 equivalent to 20 (24 - 4 = 20)
# Step is 2, so it grabs every second character.

# print(s[-20:-4:2])
# print(s[::-1])
# print(s[-15:-3:3])
# print(s[:-6:2])
# print(s[-20::3])

