a, b = map(int, input().split())

N_list1 = [i for i in range(a)]
N_list2 = [i for i in range(a)]

for i in range(a):
    N_list1[i] = input().split()

for j in range(a):
    N_list2[j] = input().split()

for i in range(a):
    for j in range(b):
        N_list1[i][j] = int(N_list1[i][j]) + int(N_list2[i][j])

for i in range(a):
    for j in range(b):
        print(N_list1[i][j], end=' ')
    print()