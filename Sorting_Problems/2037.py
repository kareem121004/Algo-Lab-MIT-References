# Problem: 2037. Minimum Number of Moves to Seat Everyone

# Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/  

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        move = 0
        for i in range(len(seats)):
            move += abs(seats[i] - students[i])
        return move

sol = Solution()
print(sol.minMovesToSeat([3,1,5],[2,7,4])) # 4