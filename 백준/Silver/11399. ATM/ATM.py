n = int(input())
p = sorted(list(map(int, input().split())))
result = 0
for i in range(len(p)):
    result += p[i]
    p[i] = result
print(sum(p))
