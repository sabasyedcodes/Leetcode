class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    count +=1
        return count
    

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.count(s,i,i) #odd length
            res += self.count(s,i,i+1) # even length
        return res

    def count(self,s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l-=1
            r+=1
        return res 