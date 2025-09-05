num = int(input())

for i in range(num):
    result = 0
    mars_math = input().split()
    for j in range(len(mars_math)):
        if mars_math[j] == '@':
            result *= 3
        elif mars_math[j] == '%':
            result += 5
        elif mars_math[j] == '#':
            result -= 7
        else:
            result += float(mars_math[j])
    print(f'{result:.02f}')
