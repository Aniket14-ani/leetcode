class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
       
        sum_sq = [0] * (4 * n)
        current_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
              
                left_node = 2 * node
                lazy[left_node] = (lazy[left_node] + val) % MOD
                len_left = mid - l + 1
                sum_sq[left_node] = (sum_sq[left_node] + 2 * val * current_sum[left_node] + val * val * len_left) % MOD
                current_sum[left_node] = (current_sum[left_node] + val * len_left) % MOD
                
                # For right child
                right_node = 2 * node + 1
                lazy[right_node] = (lazy[right_node] + val) % MOD
                len_right = r - mid
                sum_sq[right_node] = (sum_sq[right_node] + 2 * val * current_sum[right_node] + val * val * len_right) % MOD
                current_sum[right_node] = (current_sum[right_node] + val * len_right) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                lazy[node] = (lazy[node] + val) % MOD
                length = r - l + 1
                sum_sq[node] = (sum_sq[node] + 2 * val * current_sum[node] + val * val * length) % MOD
                current_sum[node] = (current_sum[node] + val * length) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            
            current_sum[node] = (current_sum[2 * node] + current_sum[2 * node + 1]) % MOD
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD

        last_occurrence = {}
        total_ans = 0
        
        for j in range(n):
            prev_idx = last_occurrence.get(nums[j], -1)
          
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            last_occurrence[nums[j]] = j
            
            total_ans = (total_ans + sum_sq[1]) % MOD
            
        return total_ans