# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
test = -11222211


def isPalindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]
    # print(test_num)
    # reverse = list(reversed(test_num))
    # print(reverse)
    # if test_num == reverse:
    #     print("Yes")
    #     return True
    # else:
    #     print('No')
    #     return False

isPalindrome(test)
