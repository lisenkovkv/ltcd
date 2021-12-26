# https://leetcode.com/problems/goal-parser-interpretation/
#string

def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    return command.replace("()",'o').replace("(al)","al")
#Runtime: 16 ms, faster than 76.52% of Python online submissions for Goal Parser Interpretation.
#Memory Usage: 13.7 MB, less than 9.15% of Python online submissions for Goal Parser Interpretation.