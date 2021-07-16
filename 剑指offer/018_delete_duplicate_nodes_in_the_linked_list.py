"""
删除链表中重复的结点: 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        next = pHead.next
        if pHead.val == next.val:
            while next != None and pHead.val == next.val:
                next = next.next
            return self.deleteDuplication(next)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead
