# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
#
#
# 示例 1:
#
# 输入:
# test_nums = [1, 2, 3, 1]
# test_k = 2


# 输出: true
# 示例 2:
#
# 输入:
test_nums = [1, 0, 1, 1]
test_k = 1


# 输出: true
# 示例 3:
#
# 输入:
# nums = [1,2,3,1,2,3]
# k = 2
# 输出: false

# 暴力法
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic or i - dic[nums[i]] > k:
            dic[nums[i]] = i
        else:
            print(True)
            return True
    print(False)
    return False


containsNearbyDuplicate(test_nums, test_k)
