n, k = map(int, input().split())

count = 0

result = [0 for i in range(12)]

for i in range(n):
    s, g = map(int, input().split())

    if s == 0 and g == 1:
        result[0] += 1
    elif s == 1 and g == 1:
        result[1] += 1

    elif s == 0 and g == 2:
        result[2] += 1
    elif s == 1 and g == 2:
        result[3] += 1

    elif s == 0 and g == 3:
        result[4] += 1
    elif s == 1 and g == 3:
        result[5] += 1

    elif s == 0 and g == 4:
        result[6] += 1
    elif s == 1 and g == 4:
        result[7] += 1

    elif s == 0 and g == 5:
        result[8] += 1
    elif s == 1 and g == 5:
        result[9] += 1

    elif s == 0 and g == 6:
        result[10] += 1
    elif s == 1 and g == 6:
        result[11] += 1

for people in result:
    if people != 0:
        if people % k == 0:
            count += (people/k)
        elif people < k:
            count += 1
        else:
            count += (people/k + 1)

print(int(count))    
