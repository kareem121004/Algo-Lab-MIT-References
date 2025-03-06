# Problem: Maximum Subsequence of Size K
# Given a list of integers nums and an integer k, return the maximum subsequence of size k.
# Problem Link : https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        n = len(nums)
        if k == 0:
            return []
        if k == n:
            return nums
        else:
            indexed_nums = [(num, i) for i, num in enumerate(nums)]
            indexed_nums.sort(reverse=True, key=lambda x: x[0])
            max_subsequence = indexed_nums[:k]
            max_subsequence.sort(key=lambda x: x[1])
            return [num for num, _ in max_subsequence]
        

sol = Solution()
print(sol.maxSubsequence([2,1,3,3], 2)) # [3,3]
print(sol.maxSubsequence([-1,-2,3,4], 3))  # [-1, 3, 4]
print(sol.maxSubsequence([3,4,3,3], 2)) # [3, 4]
print(sol.maxSubsequence([50,-75], 2)) # [50,-75]
