#Sum of first n numbers using recursion
def recursion_sum(n):
    if n<=1:
        return n
    else:
        return n + recursion_sum(n-1)
num = int(input("Enter the number of terms:"))
if num<0:
    print("Please enter a positive number")
else:
    print("The sum is:",recursion_sum(num))

#Sum of squares of first n natural numbers
def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+(i*i)
    return sum
n = int(input("Enter the number of terms:"))
print("The sum is:",square_sum(n))

#Sum of cube of first n natural numbers
def cube_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+(i*i*i)
    return sum
n = int(input("Enter the number of terms:"))
print("The sum is:",cube_sum(n))