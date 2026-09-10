class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = {0: -1}
        ps = 0

        for i in range(len(nums)):
            ps += nums[i]
            rm = ps % k

            if rm in freq:
                if i - freq[rm] >= 2:
                    return True
            else:
                freq[rm] = i

        return False