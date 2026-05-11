class Solution:
    def grayCode(self, n: int) -> List[int]:
        #Soluition 1
        #take gray code of n-1, reverse the array and store it seperately lets say new_arr
        #take new_arr and add 2^(n-1) to each number
        #finally concat the two array
        if n==1:
            return [0,1]
        
        arr = self.grayCode(n-1)
        rev_arr = arr[::-1]
        m = len(rev_arr)
        for i in range(m):
            rev_arr[i]+=2**(n-1)
        return arr+rev_arr 