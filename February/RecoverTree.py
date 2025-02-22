#1028. Recover a Tree From Preorder Traversal Feb-22/2025
class Solution(object):
    def recoverFromPreorder(self, traversal):
        index = 0
        stack = []
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()
            
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]