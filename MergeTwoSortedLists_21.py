# https://leetcode.com/problems/merge-two-sorted-lists/
#linked_list #recursion

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1,list2):
    