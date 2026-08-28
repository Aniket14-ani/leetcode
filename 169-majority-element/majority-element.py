class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        man=None
        count=0
        for i in nums:
            if count==0:
                man=i
            if i==man:
                count+=1
            else:
                count-=1
        return man           
                
              

        