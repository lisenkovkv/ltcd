#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def arrayStringsAreEqual(word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1)==''.join(word2)

#O(max(n,m)), n,m are strings lenghth. Runtime: 16 ms, faster than 90.30% of Python online submissions for Check If Two String Arrays are Equivalent.
#O(max(n,m)). Memory Usage: 13.6 MB, less than 22.42% of Python online submissions for Check If Two String Arrays are Equivalent.