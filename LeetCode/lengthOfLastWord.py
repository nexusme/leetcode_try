# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
#
# 如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。
#
#  
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
ss = "a"


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 1 or len(s) == 0:
        print(len(s))
        # return len(s)
    else:
        s = s.split(' ')
        new_s = s[len(s) - 1]
        print(len(new_s))
        return len(new_s)


lengthOfLastWord(ss)
