# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

sss = [1, 2, 3]


# 暴力法
# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     num = ''
#     for i in digits:
#         num += str(i)
#
#     new_num = int(num) + 1
#     print(new_num)
#     list = []
#     for number in str(new_num):
#         list.append(int(number))
#     print(list)

def plusOne(digits):
    length = len(digits)
    for i in reversed(range(length)):
        if digits[i] < 9:
            digits[i] += 1
            print(digits)
            return digits
        else:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                return digits

    print(digits)


plusOne(sss)
