class Solution:

    def findMinDiff(self, arr, M):
        n = len(arr)

        if M == 0 or n == 0 or M > n:
            return 0

        arr.sort()

        ans = float('inf')

        for i in range(n - M + 1):
            ans = min(ans, arr[i + M - 1] - arr[i])

        return ans
