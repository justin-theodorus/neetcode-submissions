class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res ^= (i ^ nums[i])
        return res
"""
a ^ a = 0
a ^ 0 = a

if an element is in nums, it will be xor with its index [0...n] and will produce 0

res XOR 0 wont affect the value of XOR
"""
