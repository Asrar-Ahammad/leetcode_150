def buy_and_sell_stock(arr):
    l, r = 0, 1
    max_profit = 0

    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices1 = [7, 6, 4, 3, 1]
prices3 = [1, 2, 4]
prices4 = [2,4,1]
print(buy_and_sell_stock(prices4))
