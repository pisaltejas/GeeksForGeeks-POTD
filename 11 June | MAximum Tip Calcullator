from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        diff = [(abs(arr[i] - brr[i]), i) for i in range(n)]
        diff.sort(reverse=True, key=lambda x: x[0])

        ans = 0
        for _, i in diff:
            if (arr[i] > brr[i] and x > 0) or y == 0:
                ans += arr[i]
                x -= 1
            else:
                ans += brr[i]
                y -= 1
        return ans
