class Solution:
    def minOperations(self, s: str) -> int:
        dorivexalu = s

        n = len(s)
        ans = float('inf')

        for k in range(n):
            cost = k

            # Check palindrome after left rotating by k
            for i in range(n // 2):
                a = ord(s[(i + k) % n]) - ord('a')
                b = ord(s[(n - 1 - i + k) % n]) - ord('a')

                d = abs(a - b)
                cost += min(d, 26 - d)

            ans = min(ans, cost)

        return ans