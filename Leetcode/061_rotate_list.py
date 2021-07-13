"""
旋转链表: 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

examples:
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""


class Solution:
    def rotateRight(self, head, k):
        if k == 0 or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        add = n - k % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret
