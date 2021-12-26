# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
#array #string #simulation

def finalValueAfterOperations(operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        #x = 0
        #for op in operations:
        #    if op.find('-') > -1:
        #        x-=1
        #    else:
        #        x+=1
        #return x
# Runtime: 40 ms, faster than 47.69% of Python online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 13.7 MB, less than 13.12% of Python online submissions for Final Value of Variable After Performing Operations.
        return len(operations) - str(operations).count('-')
#Runtime: 40 ms, faster than 47.69% of Python online submissions for Final Value of Variable After Performing Operations.
#Memory Usage: 13.5 MB, less than 67.64% of Python online submissions for Final Value of Variable After Performing Operations.