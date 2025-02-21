#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
#
# algorithms
# Medium (59.55%)
# Likes:    4446
# Dislikes: 91
# Total Accepted:    616.4K
# Total Submissions: 1M
# Testcase Example:  '[1,3,4,7,1,2,6]'
#
# You are given the head of a linked list. Delete the middle node, and return
# the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋^th node from the
# start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than
# or equal to x.
#
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
# respectively.
#
#
#
# Example 1:
#
#
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes
# are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
#
#
# Example 3:
#
#
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
#
#
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # 1️⃣ 리스트가 1개만 있으면 삭제 후 None 반환
        if not head or not head.next:
            return None

        # 2️⃣ 리스트 길이 찾기
        slow, fast = head, head
        prev = None  # 중간 노드의 이전 노드를 추적

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next  # fast는 2칸씩 이동 → 중간 노드 찾기

        # 3️⃣ 중간 노드 삭제 (prev가 가리키는 다음 노드를 변경)
        prev.next = slow.next

        return head  # 수정된 리스트 반환

# @lc code=end
