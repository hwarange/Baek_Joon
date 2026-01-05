n = int(input())

test = list(map(int, input().split()))
b, c = map(int, input().split())

count = 0

for i in test:
    if i <= b:
        count += 1
    else:
        result = i - b
        count += 1

        if result <= c:
            count += 1
        else:
            if result % c == 0:
                count += (result//c)
            else:
                count += (result//c) + 1

print(count)