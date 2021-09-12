# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    arr = []

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.dfs(root, 0)
        for i in range(len(self.arr)):
            if i % 2 == 1:
                self.arr[i].reverse()
        return self.arr

    def dfs(self, root, level):
        if root == None:
            return

        if level >= len(self.arr):
            self.arr.append([root.val])
        else:
            self.arr[level] += [root.val]
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)


s = Solution()




