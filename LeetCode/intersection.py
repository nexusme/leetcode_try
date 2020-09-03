import collections
# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1：
# 输入：
n1 = [1, 2, 2, 1]
n2 = [2, 2]
# 输出：[2]

# 示例 2：
# 输入：
n3 = [4, 9, 5]
n4 = [9, 4, 9, 8, 4]


# 输出：[9,4]


# 说明：
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    print((collections.Counter(nums1) & collections.Counter(nums2)).elements())
    for row in (collections.Counter(nums1) & collections.Counter(nums2)).elements():
        print(row)


intersection(n1, n2)
