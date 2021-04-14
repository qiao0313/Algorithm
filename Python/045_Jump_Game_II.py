"""
跳跃游戏 II: 给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

example:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_end, cur_farthest, step, n = 0, 0, 0, len(nums)
        for i in range(n-1):
            cur_farthest = max(cur_farthest, i + nums[i])
            if cur_farthest >= n - 1:
                step += 1
                break
            if i == cur_end:
                cur_end = cur_farthest
                step += 1

        return step


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.jump(nums))