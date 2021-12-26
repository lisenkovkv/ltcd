# https://leetcode.com/problems/reverse-words-in-a-string-iii/
#two_pointers #string

def reverseWords(s):
    
    #Approach 1
    #l=""
    #count=0
    #for x in s.split():
    #    count+=1
    #for x in s.split():
    #    l+=x[::-1]
    #        if(count>1):
    #        l+=" "
    #        count-=1
    #return l
    #Runtime: 228 ms, faster than 7.90% of Python online submissions for Reverse Words in a String III.
    #Memory Usage: 14.6 MB, less than 47.00% of Python online submissions for Reverse Words in a String III.
    
    #Approach 2
    #return ' '.join(s.split()[::-1])[::-1]
    #Runtime: 28 ms, faster than 66.95% of Python online submissions for Reverse Words in a String III.
    #Memory Usage: 14.6 MB, less than 47.00% of Python online submissions for Reverse Words in a String III.
    
    #Approach 34
    return ' '.join(x[::-1] for x in s.split())
    #Runtime: 38 ms, faster than 52.19% of Python online submissions for Reverse Words in a String III.
    #Memory Usage: 14.5 MB, less than 47.00% of Python online submissions for Reverse Words in a String III.