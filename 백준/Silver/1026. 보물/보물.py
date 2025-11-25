n = int(input())

a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))

sum_num = 0

for i in range(n):
    sum_num += b.pop(b.index(max(b))) * a[i]

print(sum_num)