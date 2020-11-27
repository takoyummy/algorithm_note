shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!

    pr = sorted(prices, reverse=True)
    cp = sorted(user_coupons, reverse=True)
    pr_index = 0
    cp_index = 0

    sum = 0

    while pr_index < len(pr) and cp_index < len(cp):
        sum += pr[pr_index] * (100 - cp[cp_index]) // 100
        pr_index += 1
        cp_index += 1

    if cp_index == len(cp):
        while pr_index < len(pr):
            sum += pr[pr_index]
            pr_index += 1
    return sum


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
