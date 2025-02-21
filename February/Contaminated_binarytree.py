#1261. Find Elements in a Contaminated Binary Tree Feb-21/2025

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class FindElements(object):

    def __init__(self, root):
        self.valid_values = set()
        if root:
            self.restore_tree(root,0)

    def find(self, target):
        return target in self.valid_values
    
    def restore_tree(self, node, value):
        if not node:
            return
        node.val = value
        self.valid_values.add(value)
        self.restore_tree(node.left, 2* value + 1)
        self.restore_tree(node.right, 2 * value + 2)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)