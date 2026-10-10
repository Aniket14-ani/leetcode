from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        count = Counter(diffs)
        
        max_diff = max(diffs)
        
        freq = [0] * (max_diff + 2)
        for d, c in count.items():
            freq[d] = c
         
        curr_k = total_k
        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue
    
            operations_needed = freq[d]
            
            if curr_k >= operations_needed:
                curr_k -= operations_needed
                freq[d] = 0
                freq[d - 1] += operations_needed
            else:
                
                freq[d] -= curr_k
                freq[d - 1] += curr_k
                curr_k = 0
                break
                
        result = 0
        for d in range(max_diff + 1):
            if freq[d] > 0:
                result += freq[d] * (d * d)
                
        return result