class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])

        row = 0
        col = m - 1
        ans = -1

        while row < n and col >= 0:
            if arr[row][col] == 1:
                ans = row
                col -= 1
            else:
                row += 1

        return ans
