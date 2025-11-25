n = int(input())

for i in range(n):
    coin = int(input())
    if coin >= 25:
        print(coin//25, end=' ')
        coin %= 25
    else:
        print(0, end=' ')

    if coin >= 10:
        print(coin//10, end=' ')
        coin %= 10
    else:
        print(0, end=' ')

    if coin >= 5:
        print(coin//5, end=' ')
        coin %= 5
    else:
        print(0, end=' ')

    if coin >= 1:
        print(coin//1)
    else:
        print(0)

