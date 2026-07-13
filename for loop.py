for i in range(1,11):
    print(i)

total=0
for i in range(1,11):
    total+=i
print("Sum=",total)

num=int(input("Enter a number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

n=int(input("Enter N:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

n=int(input("Enter a number"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)
        
