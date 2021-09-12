# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        r = self.kth(root, k)
        return r[1]

    
    def kth(self, root, k):
        if root == None:
            return False, 0

        success, n1 = self.kth(root.left, k)
        if success == True:
            return success, n1

        if n1 == k - 1:
            return True, root.val

        success, n2 = self.kth(root.right, k - n1 - 1)
        if success:
            return success, n2

        return False, n1+n2+1


    def test(self):
        
        node3 = TreeNode(3)
        node1 = TreeNode(1)
        node4 = TreeNode(4)
        node2 = TreeNode(2)
        node3.left = node1
        node3.right = node4
        node1.right = node2

        print(self.kthSmallest(node3, 1))

s = Solution()
s.test()