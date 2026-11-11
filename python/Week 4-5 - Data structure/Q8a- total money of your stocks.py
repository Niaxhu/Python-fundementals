#Create a new dictionary called prices. Put these values in your prices dictionary:
#"banana": 4, "apple": 2, "orange": 1.5, "pear": 3
#Create a stock where as "banana"= 6, "apple“ = 0, "orange" =32, "pear"= 15
#What are the total money of your stocks?

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
