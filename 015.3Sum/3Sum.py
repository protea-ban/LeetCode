class Solution0:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        # 数组题，其中有加减操作的，排序后会方便很多
        nums.sort()
        len_nums = len(nums)

        for i in range(len_nums - 1):
            for j in range(i+1, len_nums):
                # 固定下来两个数，如果另外一个数也在数组中，则为一个结果
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    a_ret = [nums[i], nums[j], -(nums[i]+nums[j])]
                    if a_ret not in ret:
                        ret.append(a_ret)

        return ret


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()

        for i in range(0, len(nums)):
            # 若存在相同数，跳过以减少计算
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            start, end = i+1, len(nums)-1

            while start < end:
                # 头尾之和大于目标值，尾向前移一位
                if nums[start] + nums[end] > target:
                    end -= 1
                # 头尾之和小于目标值，头向后移一位
                elif nums[start] + nums[end] < target:
                    start += 1
                # 头尾之和等于目标值，是一个结果，添加进去
                # 头尾都移动一位
                else:
                    ret.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    # 若移动后有重复值，继续移动
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

        return ret


if __name__ == '__main__':
    so = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(so.threeSum(nums))
