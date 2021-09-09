# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, p, q)
        return self.ans
    
    def helper(self, cur, p, q):
        if not cur:
            return False
        l = self.helper(cur.left, p, q)
        r = self.helper(cur.right, p, q)
        z = cur == p or cur == q
        if l + r + z >= 2:
            self.ans = cur
            return True
        if z  or l or r:
            return True
        return False




class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            if self.ans:
                return False
            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q
            if mid + left + right == 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = None
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node.val == p.val or node.val == q.val
            if left + mid + right >= 2:
                self.ans = node
            
            return left or mid or right
        
        dfs(root)
        return self.ans