# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            lvl = []
            levelq = []
            while q:
                node = q.popleft()
                lvl.append(node.val)
                if(node.left): levelq.append(node.left)
                if(node.right): levelq.append(node.right)
            if(len(lvl) > 0): res.append(lvl)
            q+=levelq

        return res
