class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        has_arr = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            
            has_arr[idx] = (sum(has_arr) + 1) % MOD
            
        return sum(has_arr) % MOD