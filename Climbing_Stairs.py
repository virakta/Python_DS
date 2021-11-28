# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    cache={}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in Solution.cache:
            return Solution.cache[n]
        
        if n<=3 :
            ret=n
        else:
            ret=self.climbStairs(n-1)+self.climbStairs(n-2)
        
        Solution.cache[n]=ret
        return ret