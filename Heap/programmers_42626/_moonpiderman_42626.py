import heapq
def func_scoville(first, second) :
    mix_scoville = first + (second * 2)
    return mix_scoville

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K :
        if len(scoville) > 1 :
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, func_scoville(first, second))
            answer += 1
        else :
            return -1

    return answer

if __name__ == '__main__' :
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))