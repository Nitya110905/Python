d={}
import random
acc_no = random.randint(11111111,99999999)
otp = random.randint(100001,999999)



while True:
    menu ="""
**********Welcome to Bank**********
Press 1 for Sign-Up 
Press 2 for Login
Press 3 for Forgot MPIN OR Account_No. 
Press 4 for exit
"""

    print(menu)

    choice = int(input("Enter Your choice:"))

    if choice==1: 
        print("************ Welcome To Sign-up ***************")
        mobile = int(input("Enter Mobile No. :"))
        mp = int(input("Enter MPIN :"))
        cmp = int(input("Enter Confirm MPIN :"))
        d['mp'] = mp
        # d['cmp'] = cmp 
        d['mobile'] = mobile
        if mp == cmp:
            print("Sign-Up Successful")
            print(f"Your generated Account Number is : {acc_no}")
            d['Account_No'] = acc_no
        else:
            print("MPIN and Confirm MPIN doesn't match!")

    elif choice == 2:
        print("************ Welcome To Login ***************")
        cacc_no = int(input("Enter Account No. :"))
        mp = int(input("Enter MPIN :"))

        if d['Account_No'] == cacc_no and d['mp'] == mp:
            print("Login Successful")
        
        else:
            print("Incorrect Credentials!")
    
    elif choice == 3:
        mobile = int(input("Enter Mobile no :"))

        if d['mobile'] == mobile:
            print(f"Your OTP is: {otp}")
            cotp = int(input("Enter OTP:"))
            if otp == cotp:
                mp = int(input("Reset MPIN"))
                d['mp'] = mp
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


# For multiple users, you need to apply the code like below:
# accounts = {}
# acc_no = random.randint(10000000,99999999)
# and
# accounts[acc_no] = {'mp': mp, 'mobile': mobile}


