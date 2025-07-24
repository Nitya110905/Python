# exception : when error occurs at runtime it is called exception and handle that exception called exception handling.

# 4 types:
# try : It encloses the code that might potentially raise an exception (an error). When Python executes code within a try block, it "monitors" it for any errors.

# else : This optional block contains code that should run if the code in the try block completes without raising any exceptions.

# except : It specifies what action to take when a particular exception is raised within the try block. You can have one or more except blocks to handle different types of errors.

# finally : 

# try:
#     n = int(input("Enter no. "))

#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# except ValueError as e:
#     print(e)
# else :
#     print("Try Executed!!!")
# finally:
#     print("Finally Executed!")


try:
    n = int(input("Enter no1."))
    n1 = int(input("Enter no2."))

    print("Division :",n/n1)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    l = [62,78,89,0]

    n = int(input("Enter Index:"))
    print("Value:",l[n])

except IndexError as e:
    print(e)
except ValueError as e:
    print(e)

# can be written as except (IndexError,ValueError)


try :
    n = int(input("Enter no."))
except:
    print("Invalid Choice!!!")
