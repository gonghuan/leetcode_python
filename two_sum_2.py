class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(numbers) - 1
        while head <= tail:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            elif numbers[head] + numbers[tail] < target:
                head += 1
            else:
                return [head + 1, tail + 1]
        return None

if __name__ == '__main__':
    temp = input('please enter a list:')
    nums = [int(i) for i in temp.split(' ')]
    target = int(input('please enter an int: '))
    Solution().twoSum(nums, target)
