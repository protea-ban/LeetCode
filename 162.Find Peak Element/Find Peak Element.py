class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        start = mid = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return mid


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2]
    print(so.findPeakElement(nums))
