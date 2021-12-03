n = int(input())
totalled = 0


while 9 < n:

    while n != 0:

        number = n % 10
        totalled += number
        n //= 10
    n = totalled
    totalled = 0
    #n += number


print(n+totalled)
