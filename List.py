# List is a collection data type in which we can store multiple values of different datatypes in a single variable.
# Mutable
# Orderable
# Allows duplicate values

l = [1,1.65,10,"abc",True]

# Append adds a single element at the end of list
print(type(1))
l.append(100)

print(l)

l1 = l.copy()
print(l1)

print(l.count(1))

# Extends adds multiple elements at the end of list
l.extend([300,"why",300]) 
print(l)

# Insert is used to add an element at a specific position
l.insert(2,"abc")
print(l)

# Pop is used to delete element as per index
l.pop(2)
print(l)

# Remove is used to delete element as per name
l.remove(1)
print(l)

l.reverse()
print(l)
