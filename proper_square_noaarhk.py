import math


class Solution:
    def solution(self, w: int, h: int) -> int:
        g = math.gcd(w, h)

        return w * h - (w + h - g)


if __name__ == '__main__':
    w, h = 3, 12
    sol = Solution()
    print(sol.solution(w, h))
