shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    prices_index = 0
    coupons_index = 0
    max_prices = 0

    while prices_index < len(prices) and coupons_index < len(coupons):
        max_prices += prices[prices_index] * (100-coupons[coupons_index]) / 100
        prices_index += 1
        coupons_index += 1

    while prices_index < len(prices):
        max_prices += prices[prices_index]
        prices_index +=1

    return max_prices


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))

