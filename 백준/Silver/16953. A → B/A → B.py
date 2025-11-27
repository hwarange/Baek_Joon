a, b = map(int, input().split())

count = 0

while True:
    if a == b:
        count += 1
        break
    
    elif a > b:
        count = -1
        break

    elif b % 2 != 0 and str(b)[-1] != '1':
        count = -1
        break

    elif str(b)[-1] == '1':
        b = str(b)[:len(str(b))-1]
        b = int(b)
        count += 1
        continue


    b //= 2
    count +=1

print(count)