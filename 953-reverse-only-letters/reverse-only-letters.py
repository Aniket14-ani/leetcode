class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string to a list of characters since strings are immutable in Python
        chars = list(s)
        left, right = 0, len(chars) - 1
        
        while left < right:
            # If the left character is not a letter, move the left pointer forward
            if not chars[left].isalpha():
                left += 1
            # If the right character is not a letter, move the right pointer backward
            elif not chars[right].isalpha():
                right -= 1
            # If both are letters, swap them and move both pointers
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        # Join the list back into a string and return
        return "".join(chars)

# --- Examples ---
sol = Solution()
print(sol.reverseOnlyLetters("ab-cd"))             # Output: "dc-ba"
print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))     # Output: "j-Ih-gfE-dCba"
print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!")) # Output: "Qedo1ct-eeLg=ntse-T!"