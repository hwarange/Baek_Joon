n = int(input())

for i in range(n):
    O_str = input()
    count = 0
    total = 0
    for j in O_str :
        if j == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)
