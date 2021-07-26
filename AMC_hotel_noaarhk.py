import math
from typing import List


class Solution:
    def solution(self):
        T = int(input('T:'))
        for _ in range(T):
            data = list(input('데이터를 H, W, N 순서로 기입해라 :').split())
            print(self.ans(data))

    def ans(self, data: List) -> int:
        h = int(data[0])
        n = int(data[2])

        y = math.ceil(n / h)
        if y < 10:
            y = '0' + str(y)
        x = (n % h)
        return int(str(x) + y)


if __name__ == '__main__':
    sol = Solution()
    sol.solution()
    # data = [2, [6,12,10], [30,50,72]]
