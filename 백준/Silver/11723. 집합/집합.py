import sys

input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    keyword = input().split()

    if len(keyword) == 1:
        if keyword[0] == 'all':
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else:
            s.clear()
    
    else:
        active, x = keyword[0], int(keyword[1])
        if active == 'add':
            s.add(x)

        elif active == 'remove':
            s.discard(x)
        elif active == 'check':

            if x in s:
                print(1)
            else:
                print(0)

        elif active == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    