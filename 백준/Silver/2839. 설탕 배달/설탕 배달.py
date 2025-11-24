n = int(input())

count = 0

max_num = n // 5

if max_num == 0 and n != 3:
    count = -1

else:
    for i in range(max_num, -1, -1):
        if (n - (5*i)) % 3 == 0:
            count = i + (n-(5*i)) // 3

            break

    if count == 0 and n % 3 == 0:
        count = n // 3

    elif count == 0:
        count = -1

print(count)
