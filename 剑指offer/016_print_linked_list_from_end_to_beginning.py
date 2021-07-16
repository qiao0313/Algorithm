"""
从尾到头打印链表: 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

解题思路:
1.使用递归:
要逆序打印链表 1->2->3（3,2,1)，可以先逆序打印链表 2->3(3,2)，最后再打印第一个节点 1。而链表 2->3 可以看成一个新的链表，
要逆序打印该链表可以继续使用求解函数，也就是在求解函数中调用自己，这就是递归函数。
2.使用栈:
栈具有后进先出的特点，在遍历链表时将值按顺序放入栈中，最后出栈的顺序即为逆序。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def reversePrint(self, head):
        return self.reversePrint(head.next) + [head.val] if head else []


class Solution2:
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
