import collections
from typing import List


class Solution:
    def solution(self, s: str) -> List:
        b = 0
        a = 0

        while len(s) != 1:
            s = collections.Counter(s)
            b += s['0']
            s = self._get_binary(s['1'])
            a += 1

        answer = [a, b]
        return answer

    def _get_binary(self, x: int) -> collections:
        binary_num = collections.deque()
        while x > 1:
            binary_num.appendleft(str(x % 2))
            x //= 2
        binary_num.appendleft(str(x))

        return binary_num


if __name__ == '__main__':
    sol = Solution()

    ex_1 = "110010101001"
    ex_2 = "01110"
    ex_3 = "1111111"
    """
    s 에서 0을 제외한 길이를 2진법으로 나타낸다.
    s 가 1이 될 때 까지 반복.
    ex_1>
    111111 -> 6
    
    """
    print(sol.solution(ex_1))
    print('result = [3,8]')
    print(sol.solution(ex_2))
    print('result = [3,3]')
    print(sol.solution(ex_3))
    print('result = [4,1]')
