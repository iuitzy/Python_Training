Number = int (input ("Please Enter a Number: "))

if Number % 2==0:
    print("Is Even ")
else:
    print("Is Odd ")

x= lambda a:a% 2==0
print(x(Number))