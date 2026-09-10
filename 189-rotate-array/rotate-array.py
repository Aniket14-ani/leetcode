class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        k=k%n

        ans=nums[-k:]+nums[:-k]

        for i in range(n):
            nums[i]=ans[i]
   



        