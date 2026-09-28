a = (1, 3, 3,4, 5, "kiran")
print(type(a))
print(a)

# empty tuple 
b = ()
print(type(b))

# single element tuple
c = ( 1 ,)
print(type(c)) 
#
#tuple element cant change like string,make neww tuple each time

# tuple methods 
#count how many time
no = a.count(3)
print(no)
#find index number
i = a.index(3)  #if find then stop searching
print(i)