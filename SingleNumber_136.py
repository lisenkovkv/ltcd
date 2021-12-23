# https://leetcode.com/problems/single-number/
#array #bit_manipulation

def singleNumber(nums):
    # Approach 4: Bit Manipulation
    
    a = 0
    for i in nums:
        a ^= i
    return a
#Runtime: 104 ms, faster than 85.21% of Python online submissions for Single Number.
#Memory Usage: 15.7 MB, less than 55.60% of Python online submissions for Single Number.
#Time complexity : O(n).
#Space complexity : O(1).