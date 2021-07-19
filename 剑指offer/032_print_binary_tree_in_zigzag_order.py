"""
按之字形顺序打印二叉树: 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class Solutioin:
    def print(self, root):
        ret = []
        queue = []
        queue.append(root)
        reverse = False
        while queue != None:
            tmp = []
            cnt = len(queue)
            while cnt > 0:
                node = queue.pop()
                if node == None:
                    continue
                tmp.append(node)
                queue.append(node.left)
                queue.append(node.right)
            if reverse:
                tmp = reversed(tmp)
            reverse = not reverse
            if len(tmp) != 0:
                ret.append(tmp)
        
        return ret
