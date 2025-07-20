# List is a collection data type in which we can store multiple values of different datatypes in a single variable.
# Mutable
# Orderable
# Allows duplicate values

# l = [1,1.65,10,"abc",True]
# print(type(1))

# Append adds a single element at the end of list
# l.append(100)
# print(l)

# l1 = l.copy()
# print(l1)

# print(l.count(1))

# Extends adds multiple elements at the end of list
# l.extend([300,"why",300]) 
# print(l)

# Insert is used to add an element at a specific position
# l.insert(2,"abc")
# print(l)

# Pop is used to delete element as per index
# l.pop(2)
# print(l)

# Remove is used to delete element as per name
# l.remove(1)
# print(l)

# l.reverse()
# print(l)

# l = []
# ev = []
# od = []
# for i in range(1,31):
#     l.append(i)
#     if i%2 == 0:
#         ev.append(i)
#     else:
#         od.append(i)

# print(l)
# print(ev)
# print(od)

# l = [1,2,3,1,2]
# l1 = []

# for i in l:
#     if i not in l1:
#         l1.append(i)

# print(l1)

l = [17,55,89,1,11,56]

# l.sort()

# print(f"Smallest : '{l[0]}' ")
# print(f"Greatest : '{l[-1]}' ")
# print(f"Second Largest : '{l[-2]}' ")

# n = int(input("Enter the length of list:"))

# l = []

# for i in range(1,n+1):
#     n1 = int(input("Enter List Number :"))
#     l.append(n1)
# print(l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i] , l[j] = l[j] , l[i]
print("Sorted List: ",l)



