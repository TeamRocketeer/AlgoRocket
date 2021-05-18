import collections
from math import ceil
from typing import List


# def _put_num(nl: collections.deque, m: int):
#     if m == 0:
#         nl.appendleft('4')
#     else:
#         nl.appendleft(m)


def _put_num(nl: List, m: int):
    if m == 0 or m == 3:
        nl.append('4')
    else:
        nl.append(m)

# def solution(n: int ):
#
#    pass
#
def solution(n: int) -> str:
    stack = []
    answer = []
    if n <= 3:
        _put_num(stack, n)
    else:  # n > 3
        m = n
        remainer = 0
        while m > 3:
            remainer = 3 if not remainer else m % 3
            # remainer = m % 3
            # if remainer == 0:
            #     remainer = 3
            _put_num(stack, remainer)

            m -= remainer
        _put_num(stack, m // 3)

    while stack:
        answer.append(str(stack.pop()))

    return ''.join(answer)


# stack = []
# answer = []
# while 1:
#     _put_num(stack, remainder)
#     share -= 3
#     if share == 0:
#
# while stack:
#     answer.append(str(stack.pop()))
#
#
# # while share:
# #     _put_num(stack, remainder)
# #     remainder = share % 3
# #     share //= 3
# #
# # _put_num(stack, remainder)
# #
# # while stack:
# #     answer.append(str(stack.pop()))
#
# # while share:
# #     remainder = share % 3
# #     _put_num(num_list, remainder)
# #     share //= 3
# #
# # _put_num(num_list, remainder)
# #
# return ''.join(answer)


if __name__ == '__main__':
    n = 13
    print(solution(n))
