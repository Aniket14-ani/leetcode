class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        ps = 0
        count = 0

        for i in range(len(nums)):
            ps += nums[i]
            rem = ps % k

            if rem in freq:
                count += freq[rem]

            freq[rem] = freq.get(rem, 0) + 1

        return count