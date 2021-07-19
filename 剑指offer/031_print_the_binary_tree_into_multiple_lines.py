"""
把二叉树打印成多行

example:
输入：
{1,2,3,#,#,4,5}
返回值：
[[1],[2,3],[4,5]]
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def print(self, root):
        if not root:
            return []
        res = []
        queue = []
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                r = queue.pop()
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res
