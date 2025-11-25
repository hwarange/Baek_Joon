n = int(input())

rope_list = [int(input()) for i in range(n)]
rope_list.sort(reverse=True)

max_kg = 0

for i in range(n):
    if max_kg < (rope_list[i] * (i+1)):
        max_kg = rope_list[i] * (i+1)

print(max_kg)
