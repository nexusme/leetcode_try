#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # list_num = list(nums)
    # m = 0
    sum = 0
    list = []
    for m in range(0, len(nums)):
        for i in range(m, len(nums)):
            sum += nums[i]
            list.append(sum)
        sum = 0

    print(max(list))
    print(list)


# def maxSubArray(nums）:
#     n = len(nums)
#     curr_sum = max_sum = nums[0]
#
#     for i in range(1, n):
#         curr_sum = max(nums[i], curr_sum + nums[i])
#         max_sum = max(max_sum, curr_sum)
#
#     return max_sum


maxSubArray(test)
