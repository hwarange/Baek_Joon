city_count = int(input())

road_km = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

money = 0
price = 0

for i in range(len(road_km)):
    if oil_price[i] == min(oil_price[:len(road_km)]):
        money += sum(list(map(lambda x : x * oil_price[i], road_km[i:])))
        break

    elif oil_price[i] <= oil_price[i+1]:
        price = oil_price[i]
        money += oil_price[i] * price
    
    elif i != 0 and oil_price[i] > oil_price[i-1]:
        money += oil_price[i] * price

    else:
        money += oil_price[i] * road_km[i]        

print(money)