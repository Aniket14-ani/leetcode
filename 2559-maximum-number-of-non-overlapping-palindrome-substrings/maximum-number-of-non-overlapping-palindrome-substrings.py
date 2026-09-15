class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_used = -1  
        
        for i in range(k - 1, n):
            if i - k + 1 > last_used:
                sub = s[i - k + 1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_used = i
                    continue
    
            if i - k > last_used:
                sub = s[i - k : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_used = i
                    continue
                    
        return ans