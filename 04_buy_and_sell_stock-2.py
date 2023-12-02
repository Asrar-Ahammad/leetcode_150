def buy_sell_stock(prices):
    # Solution - 1

    # l, r = 0, 1
    # profit = 0
    #
    # while r < len(prices):
    #     if prices[l] < prices[r]:
    #         profit = profit + (prices[r] - prices[l])
    #         l = r
    #     else:
    #         l = r
    #     r += 1
    # return profit

    # Solution - 2
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])

    return profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]
print(buy_sell_stock(prices2))
