class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        res = 1
        dp = [1 for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            
            res = max(res, dp[i])
        
        return res


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分查找 返回数组索引
        def binarySearch (arr, x): 

            if not arr or len(arr) == 0:
                return 0
  
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return low
        
        LIS = []
        for i in range(len(nums)):
            index = binarySearch(LIS, nums[i])
            if index == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[index] = nums[i]

        return len(LIS)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
    