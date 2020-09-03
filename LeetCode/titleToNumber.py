# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
# 输入: "A"
# 输出: 1

# 示例 2:
# 输入: "AB"
# 输出: 28

# 示例 3:
# 输入: "ZY"
# 输出: 701
test = "AAA"


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    # dic = {}
    # for i in range(65, 91):
    #     dic[chr(i)] = i - 64

    for j in range(len(s)):
        sum += (ord(s[j]) - 64) * pow(26, len(s) - 1 - j)

    print(sum)


titleToNumber(test)
