a = int(input("enter your age: "))

#if else if ladder
if (a > 18):
    print("you are the age of consent")
    print("good for you")

elif (a < 0):
    print("you are wrong")

elif (a==0):
    print("0 age is not valid")

else:
    print("you are the below the consent")