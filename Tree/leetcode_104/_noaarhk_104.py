# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth


def _to_tree(num_dq: collections.deque):
    root = TreeNode()
    current_node = root

    current_node.val = num_dq.popleft()

    # visited = []
    # 방문했던 노드 뛰어넘는 코드 필요

    while num_dq:
        print(current_node.val)

        current_node.left = TreeNode(num_dq.popleft()) if num_dq else None
        current_node.right = TreeNode(num_dq.popleft()) if num_dq else None
        if current_node.left.val:
            current_node = current_node.left
            continue
        if current_node.right.val:
            current_node = current_node.right
            continue
        print(current_node.val)


# def _to_tree(num_list: collections.deque):
#     if not num_list[0]:
#         return None
#
#     root_node = TreeNode()
#
#     while num_list:
#         head = root_node
#         if not head.val:
#             head.val = num_list.popleft()
#         else:
#             print(head.val)
#             root_node.left = TreeNode(num_list.popleft()) if num_list else None
#             root_node.right = TreeNode(num_list.popleft()) if num_list else None
#
#             if head.left:
#                 head = root_node.left
#                 _to_tree(num_list)
#             if head.right:
#                 head = root_node.right
#                 _to_tree(num_list)


if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]

    # answer: 3
    _to_tree(collections.deque(root))
    # solution = Solution()
    # print(solution.maxDepth(_to_tree(collections.deque(root))))
