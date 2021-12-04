a, b = int(input()), int(input())
counter = 0
if a == 1:
    a += 1

for i in range(a, b + 1):
    for _ in range(2, i+1):
        if i % _ == 0:
            counter += 1

    if counter == 1:
        print(i)

    counter = 0

