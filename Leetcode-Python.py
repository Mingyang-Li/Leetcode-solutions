# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def hasCycle(self, head):
        oneStpPointer = twoStepPointer = head

        while oneStpPointer and twoStepPointer:
            if oneStpPointer.next and twoStepPointer.next:
                oneStpPointer = oneStpPointer.next
                twoStepPointer = twoStepPointer.next.next
                if oneStpPointer == twoStepPointer:
                    return True
            else:
                break
        return False

    def isPalindrome(self, head):
        myList = []
        while head:
            myList.append(head.val)
            head = head.next
        return myList == myList[::-1]

    def deleteDuplicates(self, head):
        prev = curr = head
        if head == None:
            return head
        while curr:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        return head

    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        j = 0
        vowel = [0] * len(s)
        string = list(s)

        for i in range(len(string)):
            if s[i] in vowels:
                vowel[j] = string[i]
                j += 1

        for i in range(len(string)):
            if s[i] in vowels:
                j -= 1
                string[i] = vowel[j]

        return ''.join(string)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
