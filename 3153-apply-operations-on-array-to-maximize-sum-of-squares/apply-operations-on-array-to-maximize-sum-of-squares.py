class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
       
        new_nums = [0] * k
        for i in range(k):
            current_num = 0
            for j in range(32):
                if bit_counts[j] > 0:
                    current_num |= (1 << j)
                    bit_counts[j] -= 1
            new_nums[i] = current_num
            
        total_sum = 0
        for num in new_nums:
            total_sum = (total_sum + num * num) % MOD
        
        return total_sum