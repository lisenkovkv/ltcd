# https://leetcode.com/problems/single-row-keyboard/

def calculateTime(keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i
        res = 0
        temp = 0
        for c in word:
            res += abs(d[c]-temp)
            temp = d[c]
        return res
#Runtime: 24 ms, faster than 100.00% of Python online submissions for Single-Row Keyboard.
#Memory Usage: 13.6 MB, less than 45.88% of Python online submissions for Single-Row Keyboard.
        
        #pos_1 = 0
        #pos_2 = 0
        #answer = 0
        
        #for w in word:
            #pos_2 = keyboard.find(w)
            #answer += abs(pos_2 - pos_1)
            #pos_1 = pos_2
        
        #return answer
#Runtime: 44 ms, faster than 34.12% of Python online submissions for Single-Row Keyboard.
#Memory Usage: 13.8 MB, less than 10.59% of Python online submissions for Single-Row Keyboard.