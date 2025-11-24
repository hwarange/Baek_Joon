n, k = map(int, input().split())

money_list = [int(input()) for i in range(n)]

money_list.sort(reverse=True)

coin = 0

for money in money_list:
    if k >= money:
        coin += (k // money)
        k %= money


print(coin) 