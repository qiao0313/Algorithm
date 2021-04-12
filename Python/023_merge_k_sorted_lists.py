"""
合并K个升序链表:给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

example:
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""


class Solution:
    def mergeKlists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq    #堆排序
        h = []
        for lst_head in lists:
            if lst_head:
                heapq.heappush(h, (lst_head.val, lst_head))
        cur = Listnode(-1)
        dummy = cur
        while h:
            smallest_node = heapq.heappop(h)[1]
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heapq.heappush(h, (smallest_node.next.val, smallest_node.next))
        return dummy.next
