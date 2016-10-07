# Program to calculate yesterday's stock prize
# indices are minutes



def get_max_profit(my_list):

    max_profit = 0

    # loop over index and value in given stock prize
    for time, price in enumerate(my_list):
        for later_price in my_list[time+1:]:
            my_profit = later_price - price
            max_profit = max(max_profit, my_profit)

    return max_profit

print get_max_profit([10, 7, 5, 8, 11, 9])




