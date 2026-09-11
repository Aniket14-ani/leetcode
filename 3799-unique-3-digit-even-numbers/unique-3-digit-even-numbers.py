import itertools
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_nums = set()
        
        for p in itertools.permutations(digits, 3):
           
            if p[0] != 0 and p[2] % 2 == 0:
                unique_nums.add(p)
                
        return len(unique_nums)