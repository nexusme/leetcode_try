# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#

# 输入: [3,0,1]
# 输出: 2
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(0, len(nums) + 1):
        if i in nums:
            continue
        else:
            print(i)
            return i


missingNumber([0])
