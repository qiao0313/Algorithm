"""
链表中环的入口结点: 一个链表中包含环，请找出该链表的环的入口结点。要求不能使用额外的空间。

解题思路:
使用双指针，一个快指针 fast 每次移动两个节点，一个慢指针 slow 每次移动一个节点。因为存在环，所以两个指针必定相遇在环中的某个节点上。
"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        slow = pHead.next
        fast = pHead.next.next
        while slow != fast:
            fast = fast.next.next
            slow = slow.next
        fast = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
