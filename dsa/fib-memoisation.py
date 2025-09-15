class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        mem=[-1]*(n+1)
        mem[1]=1
        mem[0]=0
        def rec(n):
           
            
            if mem[n]!=-1:
                return mem[n]
                
            else:
                ans=rec(n-1)+rec(n-2)
                mem[n]=ans
                return ans
        print(mem)

                
        return rec(n)
