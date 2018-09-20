class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == '__main__':
    so = Solution()
    nums = [1,1,2,3]
    print(so.removeDuplicates(nums))
