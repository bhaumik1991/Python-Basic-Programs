#Python program to print all Prime numbers in an interval
n = int(input("Enter the number of terms:"))
for num in range(2,n+1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num)

#Python Program to check Prime Number
n = int(input("Enter a number:"))
if n>1:
    for i in range(2,n):
        if (n%i==0):
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Prime number")