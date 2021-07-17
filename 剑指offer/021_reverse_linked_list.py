"""
反转链表: 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

解题思路：
1.递归 2.迭代 3.双指针
"""


class Solution1:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead


class Solution2:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


class Solution3:
    def reverseList(self, head):
        cur, pre = None, head
        while pre != None:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t

        return cur
