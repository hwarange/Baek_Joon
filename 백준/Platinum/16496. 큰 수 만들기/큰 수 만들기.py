n = int(input())
num_list = input().split()

num_list.sort(reverse=True)

temp = 0
count = 1

if num_list[0] == '0':
    print(0)

elif len(num_list) == 1:
    print(num_list[0])

else:
    while True:
        for i in range(n-1):
            if len(num_list[i]) > len(num_list[i+1]):

                a = int(num_list[i] * len(num_list[i+1]))
                b = int(num_list[i+1] * len(num_list[i]))

                if b > a:
                    temp = num_list[i]
                    num_list[i] = num_list[i+1]
                    num_list[i+1] = temp
                    count = 1
                    break

            count = 0
        
        if count == 0:
            break

        

    for num in num_list:
        print(num, end='')


