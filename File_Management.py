# file = open("test.txt","w")
# file.write("This is write method!!")
# file.close()

# file = open("test.txt","a")
# file.write("\nThis is append method")
# file.close()

# file = open("test.txt","r")
# print(file.read())
# file.close()

# l = []

# for i in range (1,31):
#     l.append(i)

# file = open("test1.txt","w")
# file.write(str(l))
# file.close()

# file = open("test3.txt","w+")
# file.write("W+ method!!!")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# file = open("test3.txt","r+")
# print(file.read())
# file.write("Hello!")
# file.seek(0)
# print(file.read())
# file.close()

# file = open("test3.txt","a+")
# file.write("Append")
# file.seek(0)
# print(file.read())
# file.close()


d = {}
user = input("Enter common key")
name = input("Enter name")
id = int(input("Enter id"))

d[user]={
    "id":id,
    "name": name
}


file = open("test4.txt","w+")
file.write(str(d))
print(file.tell())
file.seek(0)
print(file.read())
file.close()