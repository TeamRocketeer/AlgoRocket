import heapq
from collections import Counter
from typing import List


def solution(nums: List, k: int) -> List:
    ans = []

    cnt = Counter(nums)
    print(cnt)
    for key in cnt:
        if cnt[key] >= k:
            ans.append(key)

    return ans


# heap 사용
# def heappush(heap, item):
#     """Push item onto heap, maintaining the heap invariant."""
#     heap.append(item)
#     _siftdown(heap, 0, len(heap)-1)

# def heappop(heap):
#     """Pop the smallest item off the heap, maintaining the heap invariant."""
#     lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
#     if heap:
#         returnitem = heap[0]
#         heap[0] = lastelt
#         _siftup(heap, 0)
#         return returnitem
#     return lastelt

def solution_2(nums, k):
    freqs = Counter(nums)
    freqs_heap = []
    for f in freqs:
        # heappop 은 가장 작은수를 뽑기 때문에 반대로 음수로 바꾼 빈도수를 해당 숫자와 튜블로 묶어서 heap 에 저장한다.
        heapq.heappush(freqs_heap, (-freqs[f], f))
    print(freqs_heap)
    topk = []

    # k 보다 큰 빈도수를 찾아야 하기 때문에 k 번 반복?
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution_2(nums, k))
