import collections

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 示例：
s0 = "leetcode"
# 返回 0
#
s1 = "loveleetcode"


# 返回 2


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    record = dict(collections.Counter(s))
    keep_uniq = [row for row in record]
    uniq_letter = []
    for name in keep_uniq:
        if record[name] == 1: uniq_letter.append(name)

    print(s.index(uniq_letter[0]))
    return s.index(uniq_letter[0])


firstUniqChar(s0)
