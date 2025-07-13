
def Prime_Number():
    n = int(input("Enter the no. to check whether it is prime or not : "))
    cnt = 0
    for i in range(1,n+1,1):
        if(n%i==0):
            cnt += 1

    if(cnt == 2):
        print("It is a prime no. !!")

    else:
        print("It is not a prime a no. !!")

def fibonacci_series():
    n = int(input("Enter the no. of terms you want "))
    n1 = 0 
    n2 = 1
    print(n1,end=" ")
    print(n2,end=" ")
    for i in range (3 , n+1 , 1):
        n3 = n1 + n2 
        print(n3,end=" ")
        n1 = n2
        n2 = n3 


def Reverse_number():
    n = int(input("Enter the no. to be reversed :"))
    reversed_num = 0

    while (n > 0):
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10 
        # Make use of integer division: Integer division is a type of division that discards the decimal part and returns only the whole number (integer) part of the result.

    print("Reversed number:", reversed_num)



def pattern():
    n = int(input("Enter the no. of stars you want in pattern "))


    for i in range(n,0,-1):
        for k in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end="")
        print()


while True:
    menu ="""
Press 1 for Prime number 
Press 2 for fibonacci series
Press 3 for Revrse number 
Press 4 for right angle pattern
Press 5 for exit
"""
    print(menu)
    choice = int(input("Enter The choice: "))
    
    if choice == 1:
        Prime_Number()
    elif choice == 2:
        fibonacci_series()
    elif choice == 3:
        Reverse_number()
    elif choice == 4:
        pattern()
    elif choice == 5:
        print("Thank You  for  coming !!")
        break
    else:
        print("sorry,you have not enter The Valid Choice :")
        break

