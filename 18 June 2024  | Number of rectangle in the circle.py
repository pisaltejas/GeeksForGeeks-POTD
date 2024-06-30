class Solution:
    def rectanglesInCircle(self, R):
        ans = 0
        limit = 2 * R * 2 * R
        for i in range(1, 2 * R + 1):
            for j in range(1, 2 * R + 1):
                if i * i + j * j <= limit:
                    ans += 1
        return ans
