class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
'''
        twice = 2*len(nums)
        res = []*twice
        for i in range(len(nums)):
            res.append(nums[i])
        for i in range(len(nums)):
            res.append(nums[i])
        return res
'''