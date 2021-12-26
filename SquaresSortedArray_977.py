#https://leetcode.com/problems/squares-of-a-sorted-array
#array #two_pointers #sorting

def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sq = list(map(lambda x: x ** 2, nums))
        nums_sq.sort()
        return(nums_sq)
    
#Runtime: 184 ms, faster than 86.46% of Python online submissions for Squares of a Sorted Array.
#Memory Usage: 15.6 MB, less than 57.11% of Python online submissions for Squares of a Sorted Array.