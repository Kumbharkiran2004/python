marks = {
    "kiran": 50,
    "vinay": 55,
    "sahil": 70,
    "list":[10,20,30]
}
print(type(marks))
print(marks)
#how to print indexing

print(marks["kiran"])

#dict methods
#give item keypair in tuple
print(marks.items())
# only for keys,values separataly
print(marks.keys())
print(marks.values())
#change and add new
marks.update({"kiran":85, "renuka":90})
print(marks)
#get method
print(marks.get("kiran"))  # none
print(marks["kiran"])      #key error 

b = {} #for making empty dict

#lenth
print(len(b))
