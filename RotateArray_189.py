# https://leetcode.com/problems/rotate-array/

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    #Approach 1: Brute Force
    # speed up the rotation
    #k %= len(nums)
    #for i in range(k):
    #    previous = nums[-1]
    #    for j in range(len(nums)):
    #        nums[j], previous = previous, nums[j]
    #return nums
    # Time Limit Exceeded
    # Time complexity: O(n×k). All the numbers are shifted by one step O(n) k times.
    # Space complexity: O(1). No extra space is used.
    
    #Approach 2: Using Extra Array
    #n = len(nums)
    #a = [0] * n
    #for i in range(n):
    #    a[(i + k) % n] = nums[i]
            
    #nums[:] = a
    #return nums
    #Runtime: 238 ms, faster than 20.26% of Python online submissions for Rotate Array.
    #Memory Usage: 24.9 MB, less than 68.94% of Python online submissions for Rotate Array.
    #Time complexity: O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
    #Space complexity: O(n). Another array of the same size is used.
    
    #Approach 3: Using Cyclic Replacements
    #n = len(nums)
    #k %= n
        
    #start = count = 0
    #while count < n:
    #    current, prev = start, nums[start]
    #    while True:
    #        next_idx = (current + k) % n
    #        nums[next_idx], prev = prev, nums[next_idx]
    #        current = next_idx
    #        count += 1
    #            
    #        if start == current:
    #            break
    #    start += 1
    #return(nums)
    #Runtime: 218 ms, faster than 24.91% of Python online submissions for Rotate Array.
    #Memory Usage: 24.8 MB, less than 98.08% of Python online submissions for Rotate Array.
    #Time complexity: O(n). Only one pass is used.
    #Space complexity: O(1). Constant extra space is used.
    
    #Approach 4: Using Reverse
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                

    n = len(nums)
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
        
    return(nums)
    #Runtime: 202 ms, faster than 37.64% of Python online submissions for Rotate Array.
    #Memory Usage: 24.9 MB, less than 68.94% of Python online submissions for Rotate Array.
    #Time complexity: O(n). nn elements are reversed a total of three times.
    #Space complexity: O(1). No extra space is used.