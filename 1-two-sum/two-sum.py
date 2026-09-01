class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nle= len(nums)
        for i in range(nle):
            for j in range(i+1,nle):
                if nums[i] + nums[j] == target and i!= j:
                    return[i,j]

        