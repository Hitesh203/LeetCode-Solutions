#889. Construct Binary Tree from Preorder and Postorder Traversal feb-23/2025
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def construct_tree_util(pre, post, pre_index, l, h):
            if pre_index[0] >= len(pre) or l > h:
                return None

    # The first node in preorder traversal is root
            root = TreeNode(pre[pre_index[0]])
            pre_index[0] += 1

    # no need to recur
            if l == h:
                return root

    
            i = 0
            for i in range(l, h + 1):
                if pre[pre_index[0]] == post[i]:
                    break


            if i <= h:
                root.left = construct_tree_util\
                 (pre, post, pre_index, l, i)
                root.right = construct_tree_util\
                (pre, post, pre_index, i + 1, h - 1)

            return root
        pre_index = [0]
        return construct_tree_util\
          (preorder, postorder, pre_index, 0, len(postorder) - 1)
        