class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen={}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        
        for ch in t:
            if ch in seen:
                seen[ch]-=1
            else:
                return False
            
        for val in seen.values():
            if val!=0:
                return False
        
        return True
