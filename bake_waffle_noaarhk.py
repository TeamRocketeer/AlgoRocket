from typing import List


def solution(order: List):
    f, c, x = order[0], order[1], order[2]

    # calculate time consuming
    def T(n: int) -> float:
        # t = (n * c / 2) + (x / (2 + (n * f)))
        t_staff = 0
        for j in range(n):
            t_staff += c / (2 + (j * f))
        t_order = x / (2 + (n * f))

        return t_order + t_staff

    # num of staffs start from 1 staff
    i = 1

    # initial time estimated with no staff
    t = x / 2
    while True:
        if t == T(i):
            i -= 1
            break

        t = min(t, T(i))

        if t < T(i):
            i -= 1
            break

        i += 1

    return [i, round(t, 5)]


if __name__ == '__main__':
    # f, c, x = map(int,input().split())
    # t_0 = T(0, f, c, x)
    order = [2, 10, 50]
    # order = [4, 23, 43142]
    print(solution(order))
