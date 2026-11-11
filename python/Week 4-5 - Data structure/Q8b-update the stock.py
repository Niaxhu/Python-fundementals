#If buying "banana", "orange", "apple“, update the stock

prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}
stocks = {"banana": 6,
          "apple": 0,
          "orange": 32,
          "pear": 15}

total_money = 0
for k in prices.keys():
    total_money = total_money + prices[k] * stocks[k]

print("Total money: ", total_money)

#if buy banana:
if stocks["banana"] > 0:
    stocks["banana"] = stocks["banana"] - 1

#if buy apple:
if stocks["apple"] > 0:
    stocks["apple"] = stocks["apple"] - 1