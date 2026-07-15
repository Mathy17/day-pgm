num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

for i in range(1,101):
   if i %2==0:
          print(i)
