# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first node
        node = head       
        prev = None

        while node:                   
            next_node = node.next      # remember next node
            node.next = prev           # point backward instead
            prev = node                # step prev forward
            node = next_node           # step curr forward

        return prev 