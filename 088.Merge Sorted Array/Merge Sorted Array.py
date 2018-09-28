class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1

        while i >= 0:
            if j >= 0 and k >= 0:
                if nums1[j] > nums2[k]:
                    nums1[i] = nums1[j]
                    j -= 1
                else:
                    nums1[i] = nums2[k]
                    k -= 1
            elif j >= 0:
                nums1[i] = nums1[j]
                j -= 1
            elif k >= 0:
                nums1[i] = nums2[k]
                k -= 1

            i -= 1


if __name__ == '__main__':
    so = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(so.merge(nums1, m, nums2, n))
