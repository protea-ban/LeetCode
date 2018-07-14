class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = []
        for i, num in enumerate(nums[0:-2]):
            l, r = i + 1, length - 1
            if num + nums[r] + nums[r - 1] < target:
                closest.append(num+nums[r]+nums[r-1])
            elif num+nums[l]+nums[l+1] > target:
                closest.append(num+nums[l]+nums[l+1])
            else:
                while l < r:
                    closest.append(num+nums[l]+nums[r])
                    if num+nums[l]+nums[r] < target:
                        l += 1
                    elif num+nums[l]+nums[r] > target:
                        r -= 1
                    else:
                        return target

        closest.sort(key=lambda x:abs(x-target))
        return closest[0]


if __name__ == '__main__':
    nums = [-1,0,1,1,55]
    target = 3
    solution = Solution()
    result = solution.threeSumClosest(nums, target)
    print(result)

