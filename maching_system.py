import math


class Solution:
    def solution(self, n, a, b):
        answer = 1
        final_round = math.log2(n)
        while answer < final_round:

            a = math.ceil(a / 2)
            b = math.ceil(b / 2)

            if a == b:
                break

            answer += 1

            if abs(b - a) == 1 and max(a, b) % 2 == 0:
                return answer
        return answer


if __name__ == '__main__':
    N = 8
    A = 1
    B = 2
    solution = Solution()
    print(solution.solution(N, A, B))
