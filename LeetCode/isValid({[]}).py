# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#


# 删除最小括号对 栈

test = '()'


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    # 遍历元素
    for i in s:
        # 如果都在dic中
        if stack and i in dic:
            # 且列表对应
            if stack[-1] == dic[i]:
                # 最晚入栈 即最上元素删除
                stack.pop()
            else:
                return False
        else:
            # 如果未找到匹配继续入栈
            stack.append(i)
    print(not stack)
    return not stack


isValid(test)
