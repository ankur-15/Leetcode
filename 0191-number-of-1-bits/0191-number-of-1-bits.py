class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bits = 0
        
        
        while n > 0:
            one_bits += n % 2
            n = n // 2
        
        
        return one_bits