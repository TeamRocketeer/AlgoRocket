import collections
from typing import List


def solution(properties: List, location: int) -> int:
    enum = []
    cnt = 0
    for i, v in enumerate(properties):
        enum.append((v, i))
    dq_num = collections.deque(enum)
    print(dq_num)
    while True:
        num_p = dq_num.popleft()

        if dq_num and num_p[0] < max(dq_num)[0] :
            dq_num.append(num_p)
        else:
            if num_p[1] == location:
                cnt += 1
                break
            cnt += 1
    return cnt


if __name__ == '__main__':
    '''
    [2,1,3,2] - 2 - 1
    [1,1,9,1,1,1] - 0 - 5
    
    location의 인덱스 + 1 을 리턴하면 끝
    '''
    # print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 1))
