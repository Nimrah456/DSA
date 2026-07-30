class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0,0,0]
        for i in nums:
            c[i]+=1

        a,b,d = c
        nums[:a] = [0] *a
        nums[a:a+b] = [1]*b
        nums[a+b:] = [2]*d
        
