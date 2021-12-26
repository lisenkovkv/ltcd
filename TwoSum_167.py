# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# array #two_pointers #binary_search

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    #Approach 1 Two pointer
    left = 0
    right = len(numbers) - 1
        
    while right > left:
        l = numbers[left] 
        r = numbers[right]
            
        result = l + r
            
        if result > target:
            right -= 1
        elif result < target:
            left += 1
        else: # if we have found the target
            return [left+1, right+1]
        
    return [left, right]
    #Runtime: 43 ms, faster than 83.22% of Python online submissions for Two Sum II - Input Array Is Sorted.
    #Memory Usage: 13.7 MB, less than 27.41% of Python online submissions for Two Sum II - Input Array Is Sorted.