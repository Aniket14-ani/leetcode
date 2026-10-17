class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
      
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
            
        indexed_nums = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        sorted_indexed = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
     
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            
            if visited[i] or sorted_indexed[i][2] == i:
                continue
   
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
              
                curr = sorted_indexed[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        ViewById = swaps
        return swaps