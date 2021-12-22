# https://leetcode.com/problems/power-of-two/
#math #bit_manipulation #recursion

def isPowerOfTwo(n):
#Approach 1: Bitwise Operators : Get the Rightmost 1-bit
    '''
    if n==0:
        return(False)
    return(n&(-n) == n)
    '''
#Time complexity : O(1).
#Space complexity : O(1).
#Runtime: 20 ms, faster than 61.34% of Python online submissions for Power of Two.
#Memory Usage: 13.5 MB, less than 15.06% of Python online submissions for Power of Two.

#Approach 2: Bitwise operators : Turn off the Rightmost 1-bit
    if n==0:
        return(False)
    return(n&(n-1) == 0)
#Time complexity : O(1).
#Space complexity : O(1).
#Runtime: 20 ms, faster than 61.34% of Python online submissions for Power of Two.
#Memory Usage: 13.3 MB, less than 90.74% of Python online submissions for Power of Two.

