class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i = 0
        ss = set()
        while i < len(nums):
            if nums[i] in ss:
                return True
            ss.add(nums[i])

            if i >= k:
                ss.remove(nums[i-k])
            i+=1
        return False            
        