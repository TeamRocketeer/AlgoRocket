# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        ret = str(self.val) + "\n"
        if self.left:
            ret += str(self.left)
        if self.right:
            ret += str(self.right)
        return ret


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


def _to_tree(l, i):
    if i >= len(l):
        return None
    root = TreeNode(val=l[i])
    root.left = _to_tree(l, i * 2 + 1)
    root.right = _to_tree(l, i * 2 + 2)
    return root


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
    treenode = _to_tree(root, 0)

    solution = Solution()

    print(solution.maxDepth(treenode))
