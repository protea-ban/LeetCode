class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue

            nums[j] = nums[i]
            j += 1

        return j


if __name__ == '__main__':
    so = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(so.removeElement(nums, val))
