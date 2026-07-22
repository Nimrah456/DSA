class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        for i in nums:
            if c[i] > n/2:
                return i

        

        