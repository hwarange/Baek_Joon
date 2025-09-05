hour, minute = map(int, input().split())
cookingTime = int(input())

result_minute = cookingTime+minute
if result_minute >= 60 :
    plus_hour = result_minute//60
    hour += plus_hour
    result_minute -= (60*plus_hour) 

if hour >= 24 :
    reset_hour = hour//24
    hour -= (24*reset_hour)

print(hour,result_minute) 