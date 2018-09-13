class Solution0:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 初始面积设为0
        max_area = 0

        len_h = len(height)

        for i in range(len_h):
            for j in range(i, len_h):
                area_w = j - i
                area_h = min(height[i], height[j])
                new_area = area_w * area_h
                if new_area > max_area:
                    max_area = new_area

        return max_area


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 初始化最大面积
        max_area = 0

        # 初始化两头的指针
        left = 0
        right = len(height) - 1

        # 循环
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    so = Solution()
    h = [1,8,6,2,5,4,8,3,7]
    # h = [1, 8, 6]
    ret = so.maxArea(h)
    print(ret)

