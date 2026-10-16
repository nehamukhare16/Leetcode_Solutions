# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
          
from collections import deque

class Solution:
    def levelOrder(self, root):
        # Step 1: Handle an empty tree
        if root is None:
            return []

        # Step 2: Initialize the queue and result
        queue = deque([root])
        result = []

        # Step 3: Process the tree level by level
        while queue:
            level_size = len(queue)
            level = []

            # Step 4: Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # Step 5: Add children for the next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Step 6: Save the completed level
            result.append(level)

        return result

        