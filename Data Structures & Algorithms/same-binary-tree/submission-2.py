# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # BFS or DFS for equivalent nodes, return when one node is different or a structure is different. 

        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False

        stack_1 = [p]
        stack_2 = [q]

        while len(stack_1) != 0 or len(stack_2) != 0:
            # iterate over
            # return early as soon as we find something differnt
            cur_1 = stack_1.pop()
            cur_2 = stack_2.pop()

            if (cur_1.val != cur_2.val):
                return False
            
            if cur_1.left is not None and cur_2.left is None:
                return False
            
            if cur_1.right is not None and cur_2.right is None:
                return False
            
            if cur_1.left is None and cur_2.left is not None:
                return False
            
            if cur_1.right is None and cur_2.right is not None:
                return False
            
            if cur_1.left is not None:
                stack_1.append(cur_1.left)
                stack_2.append(cur_2.left)
                
            if cur_1.right is not None:   
                stack_1.append(cur_1.right)
                stack_2.append(cur_2.right)
            


        
        return True
