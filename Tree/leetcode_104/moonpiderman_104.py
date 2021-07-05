from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        answer = 0
        if root is None :
            return answer

        queue = deque([root])
        while queue :
            answer += 1
            for _ in range(len(queue)) :
                now_node = queue.popleft()
                if now_node.left :
                    queue.append(now_node.left)
                elif now_node.right :
                    queue.append(now_node.right)

        return answer


if __name__ == '__main__' :
    # arr_1 = [3, 9, 20, None, None, 15, 7]
    # arr_2 = [1, None, 2]
    # arr_3 = []
    # arr_4 = [0]
    #
    # Sol = Solution()
    # print(Sol.maxDepth(arr_1))

    root = TreeNode()
    print(root.val)
    print(root.left)
    print(root.right)
