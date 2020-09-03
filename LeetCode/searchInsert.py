# 给定一个排序数组和一个目标值，
# 在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
#
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
test = [1, 3, 5, 6]


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for num in nums:
        if num == target:
            print(nums.index(target))
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            print(nums)
            print(nums.index(target))
            return nums.index(target)


searchInsert(test, 0)
