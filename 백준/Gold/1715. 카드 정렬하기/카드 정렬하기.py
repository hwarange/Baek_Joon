import sys
import heapq

input = sys.stdin.readline

n = int(input())

card_list = [int(input()) for i in range(n)]
heapq.heapify(card_list)
total_count = 0

while len(card_list) > 1:
    result = heapq.heappop(card_list)+heapq.heappop(card_list)
    total_count += result
    heapq.heappush(card_list, result)

print(total_count)
