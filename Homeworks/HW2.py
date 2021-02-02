
#Question 1

array = [34,3,6,8,1,98]

n = len(array)//2
array[:n],array[n:] = array[n:],array[:n]

print(array)

#Question2

n = int(input("Enter a single digit integer: "))

for i in range(n+1):
    if i % 2 == 0:
        print(i)