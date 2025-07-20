d={}
import random
otp = random.randint(1001,9999)



while True:
    menu ="""
Press 1 for Sign-Up 
Press 2 for Login
Press 3 for Mobile No. 
Press 4 for exit
"""

    print(menu)

    choice = int(input("Enter Your choice:"))

    if choice==1:
        print("************ Welcome To Sign-up ***************")
        mobile = int(input("Enter Mobile No. :"))
        email = input("Enter Email :")
        password = int(input("Enter Password :"))
        cp = int(input("Enter Confirm Password :"))
        d['email'] = email
        d['Password'] = password
        d['cp'] = cp 
        d['mobile'] = mobile
        if password == cp:
            print("Sign-Up Successful")
        else:
            print("Password and Confirm password doesn't match!")
    
    elif choice == 2:
        print("************ Welcome To Login ***************")
        email = input("Enter Email :")
        password = int(input("Enter Password :"))

        if d['email'] == email and d['Password'] == password:
            print("Login Successful")
        
        else:
            print("Incorrect Credentials!")
    
    elif choice == 3:
        mobile = int(input("Enter Mobile no :"))

        if d['mobile'] == mobile:
            print(f"Your OTP is: {otp}")
            cotp = int(input("Enter OTP:"))
            if otp == cotp:
                password = int(input("Enter Password"))
                d['Password'] = password
            else:
                print("Incorrect OTP")
        
        else:
            print("Mobile no. doesn't exist")

    elif choice == 4:
        print("Thank You!")
        break
    else:
        print("Invlaid choice!")
        break



