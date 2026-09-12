import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
       
        intervals_with_idx = [
            (intervals[i][0], intervals[i][1], intervals[i][2], i) 
            for i in range(n)
        ]
        
    
        intervals_with_idx.sort(key=lambda x: x[0])
        
        
        start_times = [x[0] for x in intervals_with_idx]
        
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
       
        for i in range(n - 1, -1, -1):
            start, end, weight, orig_i = intervals_with_idx[i]
           
            next_i = bisect.bisect_right(start_times, end)
            
            for k in range(1, 5):
                
                skip_val, skip_seq = dp[i + 1][k]
                
                take_prev_val, take_prev_seq = dp[next_i][k - 1]
                take_val = take_prev_val + weight
                take_seq = tuple(sorted(take_prev_seq + (orig_i,)))
                
                if take_val > skip_val:
                    dp[i][k] = (take_val, take_seq)
                elif take_val == skip_val:
                    
                    dp[i][k] = (take_val, min(take_seq, skip_seq))
                else:
                    dp[i][k] = (skip_val, skip_seq)
                    
        return list(dp[0][4][1])