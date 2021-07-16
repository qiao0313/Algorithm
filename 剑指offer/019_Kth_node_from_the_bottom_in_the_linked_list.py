"""
链表中倒数第 K 个结点: 输入一个链表，输出一个链表，该输出链表包含原链表中从倒数第k个结点至尾节点的全部节点。

解题思路:
设链表的长度为 N。设置两个指针 P1 和 P2，先让 P1 移动 K 个节点，则还有 N - K 个节点可以移动。此时让 P1 和 P2 同时移动，可以知道当
P1 移动到链表结尾时，P2 移动到第 N - K 个节点处，该位置就是倒数第 K 个节点。
"""


class Solution:
    def findKthToTail(self, head, k):
        if head == None:
            return None
        p1 = head
        while p1 != None and k > 0:
            p1 = p1.next
            k -= 1
        if k > 0:
            return None
        p2 = head
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
        return p2
