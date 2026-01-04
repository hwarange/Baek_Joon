n = sorted([int(input()) for _ in range(9)])

ans = sum(n) - 100

for i in range(9):
    for j in range(i+1, 9):
        if n[i] + n[j] == ans:
            n.pop(i)
            n.pop(j-1)
            break
    
    if len(n) == 7:
        break

for elem in n:
    print(elem)