# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。
#


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    # 定义前一个数字为1
    pre_num = '1'
    # 循环
    for i in range(1, n):
        # 定义下一个数字
        next_num = ''
        # 当前数字
        num = pre_num[0]
        # 重复数计数
        count = 1
        # 循环当前元素
        for j in range(1, len(pre_num)):
            # 如果有重复数字 计数
            if pre_num[j] == num:
                count += 1
            else:
                # 如果没有则构造下一个数
                next_num += str(count) + num
                # 更新num
                num = pre_num[j]
                # 更新计数
                count = 1
        # 最后两个数为上一个数的字符以及其出现次数
        next_num += str(count) + num

        pre_num = next_num
    print(pre_num)
    return pre_num


countAndSay(2)
