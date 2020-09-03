# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head:
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.next and head.val == head.next.val else head
