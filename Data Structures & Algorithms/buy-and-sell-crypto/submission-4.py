class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_buy = prices[0]
        delta = 0
     
        for i in range(len(prices)):
            if prices[i] < current_buy:
                current_buy = prices[i]
            current_delta =prices[i]-current_buy

            if current_delta > delta:
                delta = current_delta
            print(f"Current Buy: {current_buy}")
            print(f"Delta: {delta}")
            print(f"Current Delta: {current_delta}")
            print(f"Current I: {prices[i]}")

        return delta

        
        
            