class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k - 1
        total = 0
        n = len(nums)

        for i in range(l, r + 1):
            total += nums[i]

        maxsum = total

        while r < n - 1:
            total -= nums[l]
            l += 1

            r += 1
            total += nums[r]

            maxsum = max(maxsum, total)

        return maxsum / k