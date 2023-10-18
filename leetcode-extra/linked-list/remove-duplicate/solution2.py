# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def deleteDuplicates( head):

    # first make a dummy node
    dummy_head = ListNode(0)

    # attch the dummy head , to the head
    dummy_head.next = head


    # now start loop from dummy head
    current = dummy_head

    while current :

        # check if current.next == current.next.next
        if current.next and current.next.next and current.next.val == current.next.next.val:
            fixed_next = current.next
            moving_next = current.next.next

            # remove current.next.next and go for anothe next
            while  moving_next and fixed_next.val == moving_next.val:
                moving_next = moving_next.next

            # now moving_next is the last duplicate of the value
            # point current.next to moving_next.next

            print('removing:', moving_next.val)
            current.next = moving_next
            
        else:
            current = current.next

    return dummy_head.next


arr = [1,2,3,3,4,4,5]
head = ListNode(arr[0])
temp = head
for i in range(1,len(arr)):
    temp.next = ListNode(arr[i])
    temp = temp.next


newresult = deleteDuplicates( head)
print('-----')
while newresult:
    print(newresult.val)
    newresult = newresult.next

print('====================')

arr = [1,1,1,2,3]
head = ListNode(arr[0])
temp = head
for i in range(1,len(arr)):
    temp.next = ListNode(arr[i])
    temp = temp.next


newresult = deleteDuplicates( head)
print('-----')
while newresult:
    print(newresult.val)
    newresult = newresult.next

            
