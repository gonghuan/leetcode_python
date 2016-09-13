class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxList = [0 for i in range(0, len(prices))]
        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                maxList[len(prices) - 1] = prices[len(prices) - 1]
            else:
                if prices[i] > maxList[i + 1]:
                    maxList[i] = prices[i]
                else:
                    maxList[i] = maxList[i + 1]
        maxProfits = []
        for j in range(len(prices)):
            if j < len(prices) - 1:
                maxProfits.append(maxList[j + 1] - prices[j])
            else:
                maxProfits.append(0)
        result = 0
        for k in range(len(maxProfits)):
            if maxProfits[k] > result:
                result = maxProfits[k]
        return result

if __name__ == '__main__':
    temp = input('please enter a list: ')
    prices = [int(price) for price in temp.split(' ')]
    print(Solution().maxProfit(prices))
