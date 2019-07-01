#Pythn program to print Fibonacci series

n = int(input("Enter the number of terms:"))
i = 0
first_number = 0
second_number = 1
while(i<n):
    if(i<=1):
        next = i
    else:
        next = first_number+second_number
        first_number = second_number
        second_number = next
print(next)
i = i+1