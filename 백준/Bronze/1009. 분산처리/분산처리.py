
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if b % 4 == 0 :
        n_ = 4
    else:
        n_ = b % 4

    num = str(a**n_)

    if num[-1] == '0' :
        print(10)
    else:
        print(num[-1])


    