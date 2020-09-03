# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum

numm = [2, 5, 5, 10]


# 遍历法
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     lens = len(nums)
#     for i in range(0, lens - 1):
#         for j in range(1, lens):
#             if ((nums[i] + nums[j]) == target) & (i != j):
#                 print(i, j)
#                 return [i, j]
#                 break
#


# 字典 enumrate
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for ind, num in enumerate(nums):
        # 字典化
        dic[num] = ind

    for i, num in enumerate(nums):
        # 寻找目标值下标
        j = dic.get(target - num)
        if j is not None and i != j:
            print(i, j)
            return [i, j]


twoSum(numm, 10)
