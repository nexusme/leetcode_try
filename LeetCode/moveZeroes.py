# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
insert = [0, 1, 0, 3, 12]


# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    print(nums)


moveZeroes(insert)
