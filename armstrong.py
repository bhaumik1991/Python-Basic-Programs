#PYTHON PROGRAM TO CHECK ARMSTRONG NUMBER
n = int(input("Enter a number:"))
sum = 0
temp = n
while(n>0):
    digit = n%10
    sum += digit**3
    n = n//10
if(temp==sum):
    print("Armstrong number")
else:
    print("Not an Armstrong number")