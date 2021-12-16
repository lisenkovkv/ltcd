#https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # Approach 1 Two pointers technique
    #slow = 0
    #for fast in range(len(nums)):
    #    if nums[fast] != 0 and nums[slow] == 0:
    #        nums[slow], nums[fast] = nums[fast], nums[slow]
#
    #        # wait while we find a non-zero element to
    #        # swap with you
    #    if nums[slow] != 0:
    #        slow += 1
    
    #return(nums)
    #Runtime: 201 ms, faster than 29.17% of Python online submissions for Move Zeroes.
    #Memory Usage: 14.9 MB, less than 14.72% of Python online submissions for Move Zeroes.
    #Time complexity: O(n). Our fast pointer does not visit the same spot twice.
    #Space complexity: O(1). All operations are made in-placelif condition:
    
    # Approach 2 More pythonic
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return(nums)
    #Runtime: 248 ms, faster than 23.58% of Python online submissions for Move Zeroes.
    #Memory Usage: 14.7 MB, less than 63.94% of Python online submissions for Move Zeroes.