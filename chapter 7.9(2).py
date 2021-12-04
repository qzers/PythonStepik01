n = int(input())
totalled, a = 1, 0
for i in range(1, n+1):
    for _ in range(1, i+1):

        totalled *= _

    a += totalled
    totalled = 1
print(a)
