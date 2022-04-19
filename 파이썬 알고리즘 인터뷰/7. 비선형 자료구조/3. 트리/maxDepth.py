import collections


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = collections.deque([root])
        depth = 0
        while q:
            depth += 1
            for _ in range(len(q)):
                current_root = q.popleft()
                if current_root.left:
                    q.append(current_root.left)
                if current_root.right:
                    q.append(current_root.right)

        return depth