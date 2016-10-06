#Program to calculate yesterday's stock prize
#indices are minutes



def get_max_profit(my_list):
    stock_bought = min(my_list)
    stock_sold = max(my_list)
    profit = stock_sold - stock_bought
    return profit


print get_max_profit([10, 7, 5, 8, 11, 9])




