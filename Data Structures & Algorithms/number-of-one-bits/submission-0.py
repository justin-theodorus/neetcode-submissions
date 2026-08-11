class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # n - 1 flip 1 1 bit to 0, and the 0 bits after it to 1
            # at every iteration, exactly 1 1 bit will become 0
            n &= (n - 1)
            res += 1
        return res
