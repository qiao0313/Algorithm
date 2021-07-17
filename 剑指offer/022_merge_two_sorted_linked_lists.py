"""
合并两个排序的链表: 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

解题思路：
根据题目描述， 链表 l_1, l_2l 是 递增 的，因此容易想到使用双指针 l_1l 和 l_2l 遍历两链表，根据 l_1.val和
l2.val 的大小关系确定节点添加顺序，两节点指针交替前进，直至遍历完毕。
引入伪头节点： 由于初始状态合并链表中无节点，因此循环第一轮时无法将节点添加到合并链表中。
解决方案：初始化一个辅助节点 dumdum 作为合并链表的伪头节点，将各节点添加至 dumdum 之后。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2

        return dum.next
