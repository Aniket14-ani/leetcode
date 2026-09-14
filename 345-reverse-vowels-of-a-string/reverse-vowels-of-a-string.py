class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels for O(1) lookups. 
        # Make sure to include both lowercase and uppercase!
        vowels = set('aeiouAEIOU')
        
        # Convert the string to a list of characters since strings are immutable in Python
        s_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s_list) - 1
        
        while left < right:
            # Move the left pointer forward if it's not a vowel
            if s_list[left] not in vowels:
                left += 1
            # Move the right pointer backward if it's not a vowel
            elif s_list[right] not in vowels:
                right -= 1
            # If both pointers are at vowels, swap them
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        # Join the list back into a string and return
        return "".join(s_list)