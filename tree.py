# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node3 = TreeNode(3)
node1 = TreeNode(1)
node4 = TreeNode(4)
node2 = TreeNode(2)
node3.left = node1
node3.right = node4
node1.right = node2