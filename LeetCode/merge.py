# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。
#
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  
#
# 示例:
# 输入:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 2


# 输出: [1,2,2,3,5,6]


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    len_n1 = len(nums1)
    len_n2 = len(nums2)
    nums1.extend(nums2)
    del nums1[m:len_n1]
    if n < len_n2:
        del nums1[m + n: len(nums1)]
    nums1.sort()
    print(nums1)


merge(nums1, m, nums2, n)
