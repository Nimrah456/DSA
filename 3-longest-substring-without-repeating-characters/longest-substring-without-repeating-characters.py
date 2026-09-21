class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        ss = set()
        c = 0
        m = 0
        for i in range(n):
            if s[i] not in ss:
                ss.add(s[i])
                c = len(ss)
                if c > m:
                    m = c
            else:
                while s[i] in ss:#keep removing till we loose that character that repeated so what we do is we move j forward till we loose that harcter 
                    ss.remove(s[j])
                    j+=1
                ss.add(s[i])    
                c = len(ss)
        return m        






                        

        