class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [c.lower() for c in s if c.isalnum()]
        i =0
        j = len(ss)-1
        while i < j:
            if ss[i] != ss[j]:
                return False
            i+=1
            j-=1
        return True        
        