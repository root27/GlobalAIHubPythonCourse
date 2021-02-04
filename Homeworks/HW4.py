def findPrime(lower, upper):
    for i in range(lower, upper+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


findPrime(0,100)