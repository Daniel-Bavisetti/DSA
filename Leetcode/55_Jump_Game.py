class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        j=nums[0]
        for i in range(n):
            if nums[i]>j:
                j=nums[i]
            
            if i==n-1:
                return True
            if j==0:
                return False
            j-=1
        return True
