import collections
from typing import List


class Solution:
    def solution(self, n: int) -> List:
        pass

if __name__ == '__main__':
    #
    # sol = Solution()
    # sol.solution(n=4)
    n = 4
    g = collections.defaultdict(List)
    for i in range(1, n + 1):
        g[i] = [-1] * i
        g[i][0] = i
        for k in range(n):
            for j in range(1, n - 1):
                if i == n:
                    g[n][k] = n + k
                elif i == n - j:
                    g[n - j][-1] = n + k + j
                # elif i == n - 2:
                #     g[n - j][-1] = n + k + j

            # if i == n-1 :
            #
    # print(-1 in g[i] for i in range(1, n + 1))
    '''
    g[1] = 1
    g[2] = 2
    ...
    
    
    
    g[n] = n
    '''

    print(g)
