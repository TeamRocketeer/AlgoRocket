import heapq
from collections import deque
from typing import List


def scouvile(a, b):
    return a + b * 2


def my_solution(nums: List, k: int) -> int:

    nums_dq = deque(sorted(nums))
    cnt = 0

    while nums_dq[0] < k:
        nums_dq.append(scouvile(nums_dq.popleft(), nums_dq.popleft()))
        cnt += 1

        if len(nums_dq) == 1:
            break
    if nums_dq[-1] < k :
        return -1


    return cnt

def solution(nums: List, k: int) -> int:
    heap = []
    cnt = 0
    for i in nums:
        heapq.heappush(heap, i)

    while heap[0] < k:

        heapq.heappush(heap, scouvile(heapq.heappop(heap), heapq.heappop(heap)))
        cnt += 1
        # 시간복잡도 에러
        # if len(heap) == 1 and heap.pop() > k:
        #     return -1
        if len(heap) == 1:
            break

    if heap[-1] < k:
        return -1

    return cnt


if __name__ == '__main__':
    nums = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(nums, k))
