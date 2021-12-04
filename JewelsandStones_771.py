# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(jewels, stones):
        #return sum(s in jewels for s in stones) #bruteforce
#Runtime: 16 ms, faster than 82.62% of Python online submissions for Jewels and Stones.
#Memory Usage: 13.7 MB, less than 8.75% of Python online submissions for Jewels and Stones.
#Time Complexity: O(jewels\text{.length} * stones\text{.length})).
#Space Complexity: O(1) additional space complexity in Python.
        Jset = set(jewels)
        return sum(s in Jset for s in stones) # Hash Set
#Runtime: 24 ms, faster than 37.00% of Python online submissions for Jewels and Stones.
#Memory Usage: 13.5 MB, less than 60.64% of Python online submissions for Jewels and Stones.
#Time Complexity: O(J\text{.length} + S\text{.length}). The O(J\text{.length})O(J.length) part comes from creating J. The O(S\text{.length})O(S.length) part comes from searching S.
#Space Complexity: O(J\text{.length}).
