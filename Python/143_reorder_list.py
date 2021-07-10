"""
重排链表: 给定一个单链表 L：L0→L1→…→Ln-1→Ln，将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

example:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1, l2):
        while l1 and l2:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l1 = l1_temp

            l2.next = l1
            l2 = l2_temp
