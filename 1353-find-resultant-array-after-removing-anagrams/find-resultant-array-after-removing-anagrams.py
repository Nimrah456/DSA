class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            if i == 0 or sorted(words[i]) != sorted(res[-1]):
                res.append(words[i]) 
        return res

        