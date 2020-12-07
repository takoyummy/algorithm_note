import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0
    max_heap = []
    # 풀어보세요!
    while stock < k:
        for date_index in range(current_day_index, len(dates)):
            print(date_index,dates[date_index],stock,supplies[date_index])
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break
        answer += 1
        print("stock is", stock)
        stock += -heapq.heappop(max_heap)
    return answer



print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))