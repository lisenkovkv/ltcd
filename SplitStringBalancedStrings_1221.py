# https://leetcode.com/problems/split-a-string-in-balanced-strings/
from itertools import accumulate as acc

def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    return list(acc(1 if c == 'L' else -1 for c in s)).count(0)
    
    
    
    #sum = 0
    #cnt = 0
    #for c in s:
    #    if c == 'R':
    #        sum+=1
    #    else:
    #        sum-=1
    #    if sum == 0:
    #        cnt+=1
        
    #return cnt

#Runtime: 22 ms, faster than 34.83% of Python online submissions for Split a String in Balanced Strings.
#Memory Usage: 13.5 MB, less than 30.61% of Python online submissions for Split a String in Balanced Strings.