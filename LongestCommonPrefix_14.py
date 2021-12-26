# https://leetcode.com/problems/longest-common-prefix/
#string

def longestCommonPrefix(strs):
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix