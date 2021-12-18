# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    #Approach 1: Brute Force
    '''
    def check(start, end):
        chars = [0] * 128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1
            if chars[ord(c)] > 1:
                return False
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res
    '''
    #Time Limit Exceeded
    #Time complexity : O(n^3)
    #Space complexity : O(min(n, m))
    
    #Approach 2: Sliding Window
    '''
    chars = [0] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res
    '''
    #Runtime: 52 ms, faster than 66.10% of Python online submissions for Longest Substring Without Repeating Characters.
    #Memory Usage: 13.8 MB, less than 51.16% of Python online submissions for Longest Substring Without Repeating Characters.
    #Time complexity : O(n)
    #Space complexity : O(min(m, n))
    
    # Approach 3: Sliding Window Optimized (Using HashMap)
    '''
    n = len(s)
    ans = 0
        # mp stores the current index of a character
    mp = {}

    i = 0
        # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans
    '''
    #Runtime: 44 ms, faster than 82.97% of Python online submissions for Longest Substring Without Repeating Characters.
    #Memory Usage: 14.4 MB, less than 29.80% of Python online submissions for Longest Substring Without Repeating Characters.
    #Time complexity : O(n). Index jj will iterate nn times.
    #Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.
    
    #Approach 3: Sliding Window Optimized (Assuming ASCII 128)
    chars = [None] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]

        index = chars[ord(r)]
        if index != None and index >= left and index < right:
            left = index + 1

        res = max(res, right - left + 1)

        chars[ord(r)] = right
        right += 1
    return res
    #Runtime: 48 ms, faster than 74.39% of Python online submissions for Longest Substring Without Repeating Characters.
    #Memory Usage: 13.5 MB, less than 88.30% of Python online submissions for Longest Substring Without Repeating Characters.
    #Time complexity : O(n). Index jj will iterate nn times.
    #Space complexity (Table): O(m). mm is the size of the charset.