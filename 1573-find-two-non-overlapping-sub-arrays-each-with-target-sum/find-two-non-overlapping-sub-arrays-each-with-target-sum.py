class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        prefix_sums = {0: -1}
        current_sum = 0
        n = len(arr)
     
        dp = [float('inf')] * n 
        min_len_so_far = float('inf')
        ans = float('inf')
        
        for i in range(n):
            current_sum += arr[i]
            prefix_sums[current_sum] = i
           
            if current_sum - target in prefix_sums:
                start_idx = prefix_sums[current_sum - target]
                curr_len = i - start_idx
             
                if start_idx >= 0 and dp[start_idx] != float('inf'):
                    ans = min(ans, curr_len + dp[start_idx])
              
                min_len_so_far = min(min_len_so_far, curr_len)
           
            dp[i] = min_len_so_far
            
        return ans if ans != float('inf') else -1