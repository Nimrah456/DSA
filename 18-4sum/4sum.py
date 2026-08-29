class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        s = set()
        result = []
        for i in range(n):
            for j in range(i+1,n):
                k = j+1
                l = n-1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        t = (nums[i],nums[j],nums[k],nums[l])
                        if t not in s:
                            s.add(t)
                            result.append(list(t))
                        k +=1
                        l -=1
                    elif total > target:
                        l-=1
                    else:
                        k+=1
        return result   
            