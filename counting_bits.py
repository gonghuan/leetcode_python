class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                result.append(result[int(i/2)])
            else:
                result.append(result[i-1] + 1)
        return result

if __name__ == '__main__':
    temp = input('please input a number: ')
    num = int(temp)
    print(Solution().countBits(num))
