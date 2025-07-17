t = (1,2,3,"why","python")

print(type(t))
print(t.count(1))
print(t.index("why"))

l = list(t)
print(l)

# You cannot modify a tuple, so you need to convert it to list.

l.append(100)

t1 = tuple(l)

print(t1)