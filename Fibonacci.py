n = int(input("Enter thr no. of terms you want"))

n1 , n2 = 0 , 1

print(n1,n2, end=" ")
for i in range(n-2):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 , n2 = n2 , n3