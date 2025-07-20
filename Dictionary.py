# dictionary is a collection data type which store key and value pair

# mutable

# {}

# key must be unique

d = {1:"hello",2:"why",3:"Python"}
print(type(d))

# get uses key
print(d.get(1))

# To get all keys in a dictionary
print(d.keys())

# To get only values
print(d.values())

# To get both key-value pair
print(d.items())

# Remove item using key
d.pop(2)
print(d)

# Remove the last item
d.popitem()
print(d)

# Update is used to add or modify the dictionary
d.update({3:"she",4:"hello"})
print(d)

# fromKeys Used to give default value to all the keys of dictionary.
t={1,2,3,4}
d1 = {}
print(d1.fromkeys(t,20))

# Zip is used to give different values to all the keys of dictionary.
keys = ['Python', 'JS', 'HTML']
values = ['Advanced', 'Intermediate', 'Basic']
d = dict(zip(keys, values))
print(d)