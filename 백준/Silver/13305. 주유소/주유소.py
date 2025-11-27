n = int(input())

km = list(map(int, input().split()))
price = list(map(int, input().split()))

start_price = price[0]
total_money = 0

for i in range(n-1):
    if price[i] < start_price:
        start_price = price[i]
    
    total_money += km[i] * start_price
    
print(total_money)
