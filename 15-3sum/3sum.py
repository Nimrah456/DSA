class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        s = set()
        result = []
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                add = nums[j] + nums[k]
                if nums[i] + add == 0:
                    t = (nums[i],nums[j],nums[k])
                    if t not in s:
                        s.add(t)
                        result.append(list(t))
                    j +=1
                    k -=1
                elif nums[i] + add > 0:
                    k-=1
                else:
                    j+=1
        return result                        
            


        