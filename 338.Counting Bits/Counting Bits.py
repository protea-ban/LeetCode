class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num+1)
        for i in range(1, num+1):
            bits[i] += bits[i & (i - 1)] + 1
        
        return bits


class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = []
        for i in range(num+1):
            bits.append(self.hammingWeight(i))

        return bits
    
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += 1
            n &= n - 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(9))