class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        n = len(nums)
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            output[i] *= p
            p = p * nums[i]
        print(output)
        return output

if __name__ == '__main__':
    temp = input('please enter a list:')
    nums = [int(i) for i in temp.split(' ')]
    Solution().productExceptSelf(nums)
