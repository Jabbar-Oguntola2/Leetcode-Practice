class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = Counter(s), Counter(t)
        
        for c in s:
            if not (c in ct) or cs[c] != ct[c]:
                return False
        
        for c in t:
            if not (c in cs) or cs[c] != ct[c]:
                return False
        
        return True
            

