class Solution:
    def minSwap(self, arr, k):
        n = len(arr)

        # count good elements (<= k)
        good = 0
        for num in arr:
            if num <= k:
                good += 1

        # count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1

        ans = bad

        # sliding window
        left = 0
        for right in range(good, n):

            # remove left element
            if arr[left] > k:
                bad -= 1

            # add right element
            if arr[right] > k:
                bad += 1

            ans = min(ans, bad)
            left += 1

        return ans
