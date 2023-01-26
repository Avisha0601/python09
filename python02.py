month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000,30000,400,65000,100000,33000,47000,89000,4000,104000,32000,79302)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print( "The maximum profit of " + str(max_profit)+ " was record in the month of "
      + str(max_profit_month)) 

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum profit of " + str(min_profit)+ " was recorded in the month of "
      + str(min_profit_month))
