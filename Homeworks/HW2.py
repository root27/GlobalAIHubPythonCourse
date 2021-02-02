
#Question 1

array = [34,3,6,8,1,98]

if len(array) % 2 == 0:
    n = len(array)//2
    array[:n],array[n:] = array[n:],array[:n]
else:
    m = len(array) // 2
    array[:m],array[m+1:] = array[m+1:], array[:m] 



print(array)

#Question2

n = int(input("Enter a single digit integer: "))

for i in range(n+1):
    if i % 2 == 0:
        print(i)