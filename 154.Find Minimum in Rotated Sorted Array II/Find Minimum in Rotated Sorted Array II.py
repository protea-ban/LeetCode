class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return min(nums[0], nums[1])

        start = 0
        stop = len_nums - 1

        while start < stop - 1:
            if nums[start] < nums[stop]:
                return nums[start]

            mid = start + (stop - start) // 2

            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                stop = mid
            else:
                start += 1

        return min(nums[start], nums[stop])


if __name__ == '__main__':
    so = Solution()
    # nums = [2,2,2,0,1]
    nums = [1,3,5]
    print(so.findMin(nums))
