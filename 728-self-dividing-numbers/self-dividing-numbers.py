class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(num):
           
            if '0' in str(num):
                return False
            
            for digit in str(num):
                if num % int(digit) != 0:
                    return False
            
            return True

        result = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                result.append(n)
                
        return result