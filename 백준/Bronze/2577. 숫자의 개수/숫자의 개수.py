a = int(input())
b = int(input())
c = int(input())

total = str(a*b*c)
int_ ='0123456789'
count = 0

for i in int_:
    for j in total:
        if i == j :
            count += 1
    print(count)
    count = 0