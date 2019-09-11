class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        res, cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = cur_max * num, cur_min * num
            cur_min, cur_max = min(cur_max, cur_min, num), max(cur_max, cur_min, num)

            res = cur_max if cur_max > res else res
        
        return res
        