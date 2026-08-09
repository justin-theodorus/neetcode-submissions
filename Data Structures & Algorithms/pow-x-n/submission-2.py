class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binaryPow(x, n):
            """
            x^n = (x^2)^(n/2)
            """
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = binaryPow(x * x, n // 2)
            return x * res if n % 2 else res
        
        res = binaryPow(x, abs(n))
        return res if n >= 0 else 1 / res