#https://leetcode.com/problems/sorting-the-sentence/
#string #sorting


def sortSentence(s):
        """
        :type s: str
        :rtype: str
        """
        
        dict = {}

        words = s.split()
        
        for word in words:
            dict[int(word[-1])] = word[:-1]

        words_new = []

        for i in range(1,len(words)+1):
            words_new.append(dict[i])

        return(' '.join(words_new))
    
#Runtime: 16 ms, faster than 76.34% of Python online submissions for Sorting the Sentence.
#Memory Usage: 13.6 MB, less than 24.43% of Python online submissions for Sorting the Sentence.
        
        #arr = [i[-1] + i[:-1] for i in s.split()]
        
        #arr.sort()
        
        #ans = ""
        #for i in arr:
        #    ans += i[1:] + ' '
        
        #return ans[:-1]
#Runtime: 20 ms, faster than 47.84% of Python online submissions for Sorting the Sentence.
#Memory Usage: 13.4 MB, less than 94.66% of Python online submissions for Sorting the Sentence.
