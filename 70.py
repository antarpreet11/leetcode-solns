# Time - O(n), Space - O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n

        sol = [0 for i in range(n)]
        sol[0], sol[1] = 1, 2

        for i in range(2, n):
            sol[i] = sol[i-1] + sol[i-2]
        
        return sol[n-1]
    
    
# Time - O(n), Space - O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(1, n):
            temp = one + two
            one = two
            two = temp
        
        return two
