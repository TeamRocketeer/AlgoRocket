from typing import List


def _put_in(num_list: List, num: int):
    if num == 3 or num == 0:
        num_list.append(4)
    else:
        num_list.append(num)


def solution(n: int):
    stack = []
    answer = []
    num = n
    remainder = num % 3
    _put_in(stack, remainder)

    if not remainder:
        num -= 3
    else:
        num -= remainder

    share = num // 3
    while share > 3:
        stack.append(4)
        share -= 3

    if share:
        _put_in(stack, share)

    while stack:
        answer.append(str(stack.pop()))

    return str(int(''.join(answer)))


if __name__ == '__main__':
    n = 13
    print(solution(n))
