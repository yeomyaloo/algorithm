class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(node:TreeNode)->int:
            if not node:
                return -1

            #각 노드의 왼쪽, 오른쪽 리프노드(자식이 없는 잎 노드)까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)

            #상태 값

            return max(left, right) + 1
        dfs(root)
        return self.longest