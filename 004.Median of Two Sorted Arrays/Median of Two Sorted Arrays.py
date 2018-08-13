class Solution:
    def findMedianSortedArrays0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        resultList = nums1 + nums2
        resultList.sort()
        numLength = len(resultList)
        if numLength % 2 == 1:
            index = int((numLength + 1) / 2) - 1
            return resultList[index]
        else:
            index = int(numLength / 2) - 1
            return (resultList[index] + resultList[index + 1]) / 2


    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = [0] * (len(nums1) + len(nums2))

        r_i, l_i, i = 0, 0, 0
        while (l_i < len(nums1)) and (r_i < len(nums2)):
            if nums1[l_i] < nums2[r_i]:
                nums3[i] = nums1[l_i]
                l_i = l_i + 1
            else:
                nums3[i] = nums2[r_i]
                r_i = r_i + 1

            i += 1

        if l_i != len(nums1):
            nums3[i:] = nums1[l_i:]
        else:
            nums3[i:] = nums2[r_i:]

        len_3 = len(nums3)
        if len_3 % 2 != 0:
            return float(nums3[(len_3 - 1) // 2])

        return (nums3[(len_3 - 1) // 2] + nums3[len_3 // 2]) / 2





if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    su = Solution()
    result = su.findMedianSortedArrays(nums1, nums2)
    print(result)

