n = int(input())
for i in range(1, n+1):
    print(i, end='')
    for _ in range(1, i+1):
        if i % _ == 0:
            print('+', end='')
    print()

