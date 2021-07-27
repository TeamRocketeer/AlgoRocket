from typing import List


class Solution:
    def solution(self, nums: List):
        x, y, w, h = nums[0], nums[1], nums[2], nums[3]
        return min(x, y, w - x, h - y)


if __name__ == '__main__':
    nums = map(int, input().split())

