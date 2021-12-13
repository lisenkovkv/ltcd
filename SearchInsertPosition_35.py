# https://leetcode.com/problems/search-insert-position

def searchInsert(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            #pivot = (left + right) // 2
            pivot = (left + right) >> 1
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
#pivot = (left + right) // 2 :
#Runtime: 48 ms, faster than 78.04% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15.1 MB, less than 56.08% of Python3 online submissions for Search Insert Position.

#pivot = (left + right) >> 1:
#Runtime: 40 ms, faster than 98.16% of Python3 online submissions for Search Insert Position.
#Memory Usage: 15.2 MB, less than 24.26% of Python3 online submissions for Search Insert Position.

#Time complexity: O(logN)
#Space complexity : 4O(1) since it's a constant space solution.