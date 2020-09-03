# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
test1 = [0, 0, 3, 4]
test = [2, 7, 11, 15]
sum = 0


# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


def twoSum(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        dict[numbers[i]] = i
    for j in range(len(numbers)):
        tmp = target - numbers[j]
        if tmp in dict and dict[tmp] != j:
            return [j, dict[tmp]]

    return False


twoSum(test1, sum)
