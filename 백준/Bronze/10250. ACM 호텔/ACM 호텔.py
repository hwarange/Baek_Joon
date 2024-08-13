t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if (c // a) == 0 :
        print(f'{c%a}{1:02}')
    
    elif (c % a) == 0:
        print(f'{a}{(c//a):02}')
    
    else:
        print(f'{c%a}{(c//a)+1:02}')
