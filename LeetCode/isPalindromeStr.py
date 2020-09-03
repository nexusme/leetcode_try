# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
s = "A man, a plan, a canal: Panama"


def isPalindrome(s):
    getVals = list([val for val in s if val.isalnum()])
    result = "".join(getVals)
    result = result.lower()
    # print(result == result[::-1])
    return result == result[::-1]


isPalindrome(s)
