# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# 使用递归 函数调用自己
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 终止条件直到两个链表为空
    if l1 is None:
        return l2

    elif l2 is None:
        return l1

    elif l1.val <= l2.val:

        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    elif l2.val <= l1.val:
        l2.next = self.mergeTwoLists(l2.next, l1)
        return l2
