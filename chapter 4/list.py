friend = ["kiran","xyz",10,17,"isha",]
print(friend[0])

friend[0] = 'oppel'
print(friend[0])
print(friend[1:3])


# append use for add in last
friend.append("chutiya") 
print(friend)

# remove
friend.remove("chutiya")
print(friend)

# sort use for the arrange the list
l1 = [1,33,2,45,6,34,0]
l1.sort()
print(l1)

# arrange the list in reverse order
l1.reverse()
print(l1)

# for insert in the list
l1.insert(3, 894)
print(l1)
print(len(l1))  #len,max,min,sum,sorted
print(sorted(l1))

# pop
k = [1,2,3,4,5,6,7]
value = k.pop(3)
print(value)
print(k)