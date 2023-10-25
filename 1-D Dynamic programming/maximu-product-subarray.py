class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin , curmax = 1,1
        for n in nums:
            if n == 0:
                curmin , curmax = 1,1
                continue
            temp = curmax*n
            curmax = max(n*curmax,n*curmin,n)
            curmin = min(temp,n*curmin,n)
            res = max(res,curmax)
        return res
