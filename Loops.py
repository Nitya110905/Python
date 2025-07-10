# Python does not support exit controlled (do-while) loop


# while loop


# i=1
# while(i <= 10):
#     print(i)
#     i+=1

# With user-input
# n = int(input("Enter Your desired no."))
# while(i<=n):
#     print(i)
#     i+=1

# reversing
# i = int(input("Enter Your desired No."))
# while(i>=1):
#     print(i)
#     i-=1


# Even and Odd Example
# i = 1
# ev = 0
# od = 0
# evsum = 0
# odsum = 0


# while(i<=5):
#     n1 = int(input("Enter No."))
    
#     if(n1%2 == 0):
#         print(n1,"is Even")
#         ev+=1
#         evsum += n1

#     elif(n1%2 != 0):
#         print(n1,"is Odd")
#         od+=1
#         odsum += n1

#     else:
#         print(n1,"is Zero")
    
#     i+=1

# print("No. of even nos.",ev)
# print("No. of odd nos.",od)
# print("Sum of even nos.",evsum)
# print("Sum of odd nos.",odsum)



# for loop


# for i in range(1,11,1):
#     print(i)

# By default it starts from 0 and is increamented
# for i in range (10):
#     print(i)

# reverse
# for i in range (10,0,-1):
#     print(i)

# with user input
# n = int(input("Enter No."))
# for i in range (1,n+1):
#     print(i)

# reverse using user input
# n = int (input("Enter No."))
# for i in range (n,0,-1):
#     print(i)

#Even and Odd
ev = 0
od = 0
evsum = 0
odsum = 0

for i in range(5):
    n = int(input("Enter 5 no.s"))
    if(n%2 == 0):
        print(n,"is Even")
        ev+=1
        evsum += n

    elif(n%2 != 0):
        print(n,"is Odd")
        od+=1
        odsum += n

    else:
        print(n,"is Zero")
    
print("No. of even nos.",ev)
print("No. of odd nos.",od)
print("Sum of even nos.",evsum)
print("Sum of odd nos.",odsum)


 