# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
test = [3, 3, 4]
# 输出: 3
# 示例 2:
#
test1 = [2, 2, 1, 1, 1, 2, 2]

# 输出: 2

test3 = [-1, 100, 2, 100, 100, 4, 100]


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dic = {}
    for i in nums:
        dic[i] = nums.count(i)
    print(max(dic, key=dic.get))


majorityElement(test)
