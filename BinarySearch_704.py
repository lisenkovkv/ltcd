# https://leetcode.com/problems/binary-search/

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            #print(f'pivot: {pivot}')
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
                #print(f'right {right}')
            else:
                left = pivot + 1
                #print(f'left: {left}')
        return -1

# Runtime: 196 ms, faster than 85.78% of Python online submissions for Binary Search.
# Memory Usage: 14.6 MB, less than 83.18% of Python online submissions for Binary Search.
# Time complexity : O(logN).
# Space complexity : O(1)