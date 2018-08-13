### 描述
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

### Example

    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
    
### 思路
1. 这是大佬的代码，没怎么看懂
2. 大概意思是使用递归的思想，将 n 数之和转换成了 n-1 数之和再加一个数
3. 前段时间刚看过递归相关的知识，消化一下再回来看这个