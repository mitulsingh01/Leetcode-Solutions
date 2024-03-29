# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None: return  l2
        if l2 == None: return l1
        if l1.val > l2.val:
            temp = l1
            l1 = l2
            l2 = temp
        res = l1
        while l1 and l2:
            temp = None
            while l1 and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            temp.next = l2
            
            temp = l1
            l1 = l2
            l2 = temp
        return res
        
        
        
        
        
        """if l1 == None:
            return  l2
        if l2 == None:
            return l1
        #implementing recursion to get the next node of the list 
        if l1.val <= l2.val:
            curr = l1
            curr.next = self.mergeTwoLists(l1.next,  l2)
        else:
            curr = l2
            curr.next = self.mergeTwoLists(l1,  l2.next)
        #returning the head 
        return curr"""