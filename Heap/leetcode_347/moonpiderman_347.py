import heapq
from collections import Counter

def solution_1(nums, k) :
    check = []
    answer = []
    count = 0
    heapq.heapify(nums)
    if len(nums) == k :
        return nums
    while nums :
        what = heapq.heappop(nums)
        # print(nums)
        if len(nums) == 0 :
            count += 1
            check.append([what, count])
            break
        else :
            next = heapq.heappop(nums)
            if what == next :
                count += 1
                heapq.heappush(nums, next)
            else :
                count += 1
                check.append([what, count])
                count = 0
                heapq.heappush(nums, next)

    # print(check)

    for i in range(len(check)) :
        if check[i][1] >= k :
            answer.append(check[i][0])
    return answer

def solution(nums, k) :
    answer = []
    dic = Counter(nums)
    if len(nums) == k :
        return nums
    for key, value in dic.items() :
        if value >= k :
            answer.append(key)
    return answer

if __name__ == '__main__' :
    nums_1 = [1, 1, 1, 2, 2, 3]
    k_1 = 2
    nums_2 = [1]
    k_2 = 1
    nums_3 = [1, 2]
    k_3 = 2
    nums_4 = [3, 0, 1, 0]
    k_4 = 1

    print(solution(nums_3, k_3))
    print(solution_1(nums_3, k_3))
    print(solution(nums_4, k_4))
    print(solution_1(nums_4, k_4))


