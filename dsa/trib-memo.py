class Solution:
    def tribonacci(self, n: int) -> int:
        if n>2:
            mem=[-1]*(n+1)
            mem[0]=0
            mem[1]=1
            mem[2]=1
        
        def rec(n):
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            if mem[n]==-1:
                
                ans=rec(n-1)+rec(n-2)+rec(n-3)
                mem[n]=ans
            return mem[n]

        return rec(n)
        
