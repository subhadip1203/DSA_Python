# https://leetcode.com/problems/reverse-linked-list-ii/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(5)


class Solution:
    def reverseBetween(self, head, left, right):

        beforestart = None
        afterEnd = None
        start = None
        end = None

        i = 1
        current = head
        while current:
            if i == left-1:
                beforestart = current
            if i == left :
                start = current
            if i == right:
                end = current
            if i == right+1:
                afterEnd = current

            current= current.next
            i+= 1

        

        def reverseGeneral(head , end , afterEnd):
            prev = None
            current = head
            while current and current != afterEnd :
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return [prev, head]
        
        result = reverseGeneral(start , end , afterEnd)
        
        beforestart.next = result[0] 
        result[1].next = afterEnd


        current = head
        while current:
            print(current.val ,end="->")
            current = current.next

    




print(Solution().reverseBetween(Head , 2,4))
        