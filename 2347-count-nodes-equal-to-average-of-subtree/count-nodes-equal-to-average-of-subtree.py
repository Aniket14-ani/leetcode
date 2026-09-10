

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def post_order(node):
          
            if not node:
                return 0, 0, 0
            
            left_sum, left_count, left_matches = post_order(node.left)
            right_sum, right_count, right_matches = post_order(node.right)
            
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count
      
            current_matches = left_matches + right_matches
            
           
            if current_sum // current_count == node.val:
                current_matches += 1
                
            return current_sum, current_count, current_matches
            
       
        _, _, total_matches = post_order(root)
        return total_matches