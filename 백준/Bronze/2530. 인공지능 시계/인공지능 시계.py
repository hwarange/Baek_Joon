hour, minute, second = map(int, input().split())
cookingTime = int(input())

result_second = cookingTime+second

if result_second >= 60 :
    plus_minute = result_second//60
    minute += plus_minute
    result_second -= (60*plus_minute)

if minute >= 60 :
    plus_hour = minute//60
    hour += plus_hour
    minute -= (60*plus_hour)  

if hour >= 24 :
    reset_hour = hour//24
    hour -= (24*reset_hour)

print(hour,minute,result_second) 