# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # n1 = []
        # n2 = []
        # while l1 != None:
        #     n1.append(l1.val)
        #     l1 = l1.next
        # while l2 != None:
        #     n2.append(l2.val)
        #     l2 = l2.next
        # n1.reverse()
        # n2.reverse()

        # carry = 0
        # i = 0
        # head = None
        # last = None
        # while i < len(n1) or i < len(n2) or carry > 0:
        #     if i < len(n1):
        #         carry += n1[i]
        #     if i < len(n2):
        #         carry += n2[i]
        #     node = ListNode(carry % 10, None)
        #     if last == None:
        #         head = node
        #         last = node
        #     else:
        #         last.next = node
        #         last = node

        #     carry = carry // 10
        #     i += 1

        head = None
        carry = 0
        while l1 != None or l2 != None or carry > 0:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            node = ListNode(carry % 10, None)
            if last == None:
                head = node
                last = node
            else:
                last.next = node
                last = node
            carry = carry // 10

        return head
