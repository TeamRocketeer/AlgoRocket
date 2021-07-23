from typing import List


def solution(lottos: List, win_nums: List) -> List:
    w = 0
    z = 0

    for num in lottos:
        if num == 0:
            z += 1
        elif num in win_nums:
            w += 1

    hits = [z + w, w]

    for i in range(len(hits)):
        if hits[i] == 6:
            hits[i] = 1
        elif hits[i] == 5:
            hits[i] = 2
        elif hits[i] == 4:
            hits[i] = 3
        elif hits[i] == 3:
            hits[i] = 4
        elif hits[i] == 2:
            hits[i] = 5
        else:
            hits[i] = 6

    return hits

def solution_2(lottos, win_nums):

    # if 문이 아니라 딕셔너리의 키와 아이템으로 표현
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    # 포인터를 돌리는게 아닌 교집합의 갯수와 0의 갯수로 당첨 숫자를 카운트 했다.
    a = rank[len(set(lottos) & set(win_nums)) + lottos.count(0)]
    b = rank[len(set(lottos) & set(win_nums))]
    return [a, b]


if __name__ == '__main__':
    lottos_1 = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    answer = [3, 5]

    print(solution(lottos_1, win_nums))
