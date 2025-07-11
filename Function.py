# A function is a block of code executed everytime on calling.

# There are 2 Types Of functions
# 1. Built-in : input,print
# 2. User-Defined 
# -> There Are 4 types of user - defined Function 
# a.) Function without parameter without returntype
# b.) Function with parameter with returntype
# c.) Function without parameter with returntype
# d.) Function with parameter without returntype

# Parameters-At the time of declaration.
# Argument- At the time of calling.


# 1. Function without parameter, without return type

# Declaration
# def func():
    # print("Hello function")

# Calling
# func()


# 2. Function with parameter, without return-type

# def func1(n1,n2,n3):
#     if(n1>n2):
#         if(n1>n3):
#             print("Greatesst no. is ",n1)
#         else:
#             print("Greatest no. is ",n3)
#     elif(n2>n3):
#         print("Greatest no. is ",n2)
#     else:
#         print("Greatest no. is ",n3)

# n4 = int(input("Enter First no."))
# n5 = int(input("Enter Second no."))
# n6 = int(input("Enter Third no."))
# func1(n4,n5,n6)

# def func2(n):
#     for i in range(0,n):
#       for j in range(0,i+1):
#         print("*",end=" ")
    
#       print()

# a = int(input("Enter the no. of rows you want"))
# func2(a)


# 3. Function without parameter, with return type

# def func3():
#     n4 = int(input("Enter First no."))
#     n5 = int(input("Enter Second no."))
#     n6 = int(input("Enter Third no."))
    
#     if(n4>n5):
#         if(n4>n6):
#             return n4
#         else:
#             return n6
#     elif(n5>n6):
#         return n5
#     else:
#         return n6
    
# print(func3())


# 4. Functions with parameter, with return type

def func4(n):
    n1 , n2 = 0 , 1
    print(n1,n2,end=" ")
    for i in range (n-2):
        n3 = n1 + n2 
        print(n3,end=" ")
        n1 , n2 = n2 , n3
    return n3


a = int(input("Enter the no. of terms you want: "))
print("Fibonacci for ", a ," terms : ", end=" ")
last_term = func4(a)
print("\nThe", a, "th term in the series is:", last_term)



# Python uses duck typing, meaning it focuses on behavior rather than explicit types.

# When you write def func(int n), you're using a syntax borrowed from statically typed languages like Java or C++, which expect type declarations during function definition.