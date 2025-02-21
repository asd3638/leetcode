#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (61.81%)
# Likes:    10517
# Dislikes: 552
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
#
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
#
# Constraints:
#
#
# The number of nodes in the linked list is in the range [0, 10^4].
# -10^6 <= Node.val <= 10^6
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # 노드가 0개 또는 1개라면 변경할 필요 없음

        odd = head  # 첫 번째 노드 (홀수 노드의 시작)
        even = head.next  # 두 번째 노드 (짝수 노드의 시작)
        even_head = even  # 짝수 노드의 시작을 저장

        while even and even.next:
            odd.next = even.next  # 홀수 노드가 다음 홀수 노드를 가리킴
            odd = odd.next  # 다음 홀수 노드로 이동
            even.next = odd.next  # 짝수 노드가 다음 짝수 노드를 가리킴
            even = even.next  # 다음 짝수 노드로 이동

        odd.next = even_head  # 홀수 노드 리스트 끝을 짝수 노드 리스트의 시작과 연결

        return head  # 변경된 연결 리스트 반환
# @lc code=end
