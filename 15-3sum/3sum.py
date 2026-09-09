class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        a = set()
        result = []
        for i in range(n):
            j = i+1
            l = n-1
            while j < l:
                add = nums[j] + nums[l]
                if nums[i] + add == 0:
                    t = (nums[i],nums[j],nums[l])
                    if t not in a:
                        a.add(t)
                        result.append(list(t))
                    j +=1
                    l -=1
                elif nums[i] + add > 0:
                    l-=1
                else:
                    j+=1
        return result                        
            


        