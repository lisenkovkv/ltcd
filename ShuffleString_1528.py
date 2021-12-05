# https://leetcode.com/problems/shuffle-string/

def restoreString(s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        #return ''.join([v for (_,v) in sorted(zip(indices, s))])
#Runtime: 44 ms, faster than 55.12% of Python online submissions for Shuffle String.
#Memory Usage: 13.5 MB, less than 39.06% of Python online submissions for Shuffle String.
        res = [''] * len(s)
        for index, char in enumerate(s):
            res[indices[index]] = char
        return "".join(res)
#Runtime: 40 ms, faster than 74.33% of Python online submissions for Shuffle String.
#Memory Usage: 13.6 MB, less than 39.06% of Python online submissions for Shuffle String.