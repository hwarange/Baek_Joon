def solution(number:int, n:int, m:int):
    answer = 1 if number % n == 0  and number % m == 0 else 0
    return answer