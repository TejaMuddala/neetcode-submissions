class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        
        cc = {}

        for char in s:
            cc[char] = cc.get(char,0) +1
        
        for char in t:
            if char not in cc or cc[char] == 0:
                return false
            cc[char] -= 1
        
        return all(count == 0 for count in cc.values())