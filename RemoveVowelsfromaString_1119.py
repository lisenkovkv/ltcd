#https://leetcode.com/problems/remove-vowels-from-a-string
import re

def removeVowels(s):
    """
    :type s: str
    :rtype: str
    """
    #return s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
        #Runtime: 30 ms, faster than 5.93% of Python online submissions for Remove Vowels from a String.
        #Memory Usage: 13.5 MB, less than 63.70% of Python online submissions for Remove Vowels from a String.
    #return "".join(c for c in s if c not in "aeiou")
        #Runtime: 24 ms, faster than 21.48% of Python online submissions for Remove Vowels from a String.
        #Memory Usage: 13.3 MB, less than 89.63% of Python online submissions for Remove Vowels from a String.
    return re.sub('a|e|i|o|u', '', s)
        #Runtime: 19 ms, faster than 52.59% of Python online submissions for Remove Vowels from a String.
        #Memory Usage: 13.2 MB, less than 97.78% of Python online submissions for Remove Vowels from a String.
    #retval = []
    #vowels = set('aeiou')
    #for letter in s:
        #if letter not in vowels:
            #retval.append(letter) 
    #return ''.join(retval)
        #Runtime: 24 ms, faster than 21.48% of Python online submissions for Remove Vowels from a String.
        #Memory Usage: 13.3 MB, less than 97.78% of Python online submissions for Remove Vowels from a String.