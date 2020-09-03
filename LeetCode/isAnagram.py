# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s = sorted(s)
    t = sorted(t)
    print(s == t)


isAnagram("anagram", "nagaram")
