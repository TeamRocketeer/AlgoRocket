
def solution(n: int):
    num = n
    stack = []
    while num:
        remainder = num % 3
        if remainder == 0:
            remainder = 4
            num -= 1
        stack.append(remainder)
        num //= 3
    answer = []
    while stack:
        answer.append(str(stack.pop()))

    return ''.join(answer)



if __name__ == '__main__':
    n = 6
    print(solution(n))
