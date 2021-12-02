# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if op.find('-') > -1:
                x-=1
            else:
                x+=1
        return x