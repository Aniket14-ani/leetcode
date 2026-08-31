class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                maxi, mini = mini, maxi

            maxi = max(num, maxi * num)
            mini = min(num, mini * num)

            ans = max(ans, maxi)

        return ans