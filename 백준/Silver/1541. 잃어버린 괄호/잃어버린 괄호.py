n = input().split('-')

total = 0

if len(n) == 1:
    n[0] = map(int, n[0].split('+'))
    print(sum(n[0]))

else:
    if n[0].find('+') != -1:
        n[0] = sum(map(int, n[0].split('+')))
        total += n[0]

    else:
        total += int(n[0])

    for i in range(1, len(n)):
        if n[i].find('+') != -1:
            n[i] = sum(map(int, n[i].split('+')))
        
        total -= int(n[i])

    print(total)

        