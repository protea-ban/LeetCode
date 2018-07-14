### 描述
> Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Example
    Given array nums = [-1, 2, 1, -4], and target = 1.
    
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
### 思路
1. 将整个列表按照从小到大排序。
2. 固定第一个数，l代表最左边数的下标，r代表最右边数的下标。
3. 如果固定数+nums[r]+nums[r-1]小于目标值，此固定数与数组中任意两个数之和都小于目标值，且最接近目标值得便是这三个数。将三数之和append到最优列表中。
4. 如果固定数+nums[l]+nums[l+1]大于目标值，此固定数与数组中任意两个数之和都大于目标值，且最接近目标值得便是这三个数。将三数之和append到最优列表中。
5. 若不满足3、4：
    1. 将固定数+nums[l]+nums[r]之和append到最优列表中。
    2. 若三数之和小于目标值，l右移
    3. 若三数之和大于目标值，r右移
    4. 若三数之和等于目标值，直接返回（最优值只有一个）