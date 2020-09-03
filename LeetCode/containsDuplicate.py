# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
t = [1, 2, 3, 1]

# 输出: true
# 示例 2:
#
t1 = [1, 2, 3, 4]

# 输出: false
# 示例 3:
#
t3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

t4 = [2, 14, 18, 22, 22]


# 暴力法
# def containsDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     nums.append(-1)
#     l = list(nums)
#     print(l)
#     for i in nums:
#         print(i, l.count(i))
#         if l.count(i) > 1:
#             print(True)
#             return True
#
#     return False
#

def containsDuplicate(nums):
    return len(nums) > len(set(nums))


containsDuplicate(t1)
