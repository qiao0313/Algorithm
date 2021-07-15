"""
和为 S 的连续正数序列: 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

解题思路：
设连续正整数序列的左边界 ii 和右边界 jj ，则可构建滑动窗口从左向右滑动。循环中，每轮判断滑动窗口内
元素和与目标值 target 的大小关系，若相等则记录结果，若大于 target 则移动左边界 ii （以减小窗口内的元
素和），若小于 target 则移动右边界 jj （以增大窗口内的元素和）。
"""


class Solution:
    def findContinuousSequence(self, target):
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j

        return res


if __name__ == '__main__':
    target = 9
    s = Solution()
    print(s.findContinuousSequence(target))
