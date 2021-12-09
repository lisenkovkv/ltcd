#https://leetcode.com/problems/sorting-the-sentence/

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