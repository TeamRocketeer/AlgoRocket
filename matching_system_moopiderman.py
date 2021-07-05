import math
def solution_fail(n, a, b):
    answer = 0

    while n > 0 :
        div = n // 2
        if a <= div and b > div :
            while div > 0 :
                div //= 2
                answer += 1
            return answer

        else :
            while div > 0 :
                div //= 2
                answer += 1
            return answer


def solution(n, a, b):
    if a > b :
        a, b = b, a
    answer = 1
    final_round = math.log2(n)

    if a % 2 == 1 and b % 2 == 0 :
        if abs(a - b) == 1 :
            return 1

    while answer < final_round:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            return answer
    return answer

if __name__ == '__main__' :
    n = 8
    a = 4
    b = 7

    print(solution(n, a, b))