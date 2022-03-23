# Task 1 
a = 1
a = 1
a = 1 

print(id(a))

# Task 2 
c = 2
b = 2

print(id(c))
print(id(b))

# Task 3 
del(a)
del(b)
del(c)

a = 1
b = 1
c = 1

print(id(a))
print(id(b))
print(id(c))

del(c)

c = 3
c = 3
print(id(c))