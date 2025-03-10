# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if k == 1:
            return 0
        res = float('inf') # float('inf') is used to represent positive infinity
        for i in range(n - k + 1):
            res = min(res, nums[i + k - 1] - nums[i])
        return res

sol = Solution()
print(sol.minimumDifference([90], 1)) # 0
print(sol.minimumDifference([9,4,1,7], 2)) # 2
print(sol.minimumDifference([87063,61094,44530,21297,95857,93551,9918], 6)) # 74560
