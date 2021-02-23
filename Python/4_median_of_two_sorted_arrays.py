"""
寻找两个正序数组的中位数:给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

example:
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
"""

from math import floor

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type num1: List[int]
        :type num2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, floor(n/2)+1)
        else:
            smallar = self.findKth(nums1, nums2, floor(n/2))
            bigger = self.findKth(nums1, nums2, floor(n/2)+1)
            return (smallar + bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])

        a = A[floor(k/2)-1] if len(A) >= k/2 else None
        b = B[floor(k/2)-1] if len(B) >= k/2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[floor(k/2):], B, k - floor(k/2))
        else:
            return self.findKth(A, B[floor(k/2):], k - floor(k/2))

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    s = Solution()
    m = s.findMedianSortedArrays(nums1, nums2)
    print(m)