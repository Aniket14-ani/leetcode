class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count the number of 'W's in the first window of size k
        current_w_count = blocks[:k].count('W')
        min_operations = current_w_count
        
        # Slide the window through the rest of the string
        for i in range(k, len(blocks)):
            # If the new block entering the window is 'W', increment our count
            if blocks[i] == 'W':
                current_w_count += 1
            
            # If the old block leaving the window was 'W', decrement our count
            if blocks[i - k] == 'W':
                current_w_count -= 1
                
            # Update the minimum operations needed
            min_operations = min(min_operations, current_w_count)
            
        return min_operations