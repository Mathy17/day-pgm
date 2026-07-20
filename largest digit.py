num=int(input("Enter a number:"))
count=0
while num>0:
    digit=num%10
if digit%2==0:
     count+=1
     num=num//10
print("Even digit count:",count)


num=int(input("Enter a number:"))
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    num=num//10
print("Largest digit:",largest)
