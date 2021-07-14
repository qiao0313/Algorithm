"""
最小的K个数: 给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

解题思路：快速排序
"""


class Solution:
    def getLeastNumber(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]

    def quick_sort(self, lst):
        if not lst:
            return []
        pivot = lst[0]
        left = self.quick_sort([x for x in lst[1:] if x < pivot])
        right = self.quick_sort([x for x in lst[1:] if x >= pivot])

        return left + [pivot] + right


if __name__ == '__main__':
    tinput = [4,5,1,6,2,7,3,8]
    s = Solution()
    print(s.getLeastNumber(tinput, 4))