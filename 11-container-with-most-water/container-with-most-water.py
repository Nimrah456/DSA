class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        area = 0
        while i < j:
            w = j - i
            l = min(height[i], height[j])
            a = w*l
            area = max(area,a)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return area             
        