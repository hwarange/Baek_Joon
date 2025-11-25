n = int(input())

coin = 1000 - n
count = 0

if coin >= 500:
    count += coin//500
    coin %= 500 

if coin >= 100:
    count += coin//100
    coin %= 100 

if coin >= 50:
    count += coin//50
    coin %= 50 

if coin >= 10:
    count += coin//10
    coin %= 10

if coin >= 5:
    count += coin//5
    coin %= 5

if coin >= 1:
    count += coin//1
    coin %= 1

print(count)


