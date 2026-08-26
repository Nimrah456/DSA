class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #cleaning
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+99
        for i in range(n):
            value = abs(nums[i])
            if value <= n:
                index = value - 1
                nums[index] = -(abs(nums[index]))
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1             
                  

        