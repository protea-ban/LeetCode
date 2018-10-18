class Solution1:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(0, len(nums)+1):
            ret ^= i

        for num in nums:
            ret ^= num

        return ret


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0

        for i in range(0, len(nums)+1):
            sum1 += i

        for num in nums:
            sum2 += num

        if sum1 == sum2:
            return 0
        else:
            return sum1 - sum2


if __name__ == '__main__':
    so = Solution()
    nums = [3, 2, 1]
    print(so.missingNumber(nums))
