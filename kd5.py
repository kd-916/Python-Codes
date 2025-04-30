prices = {"Rice": 50, "Sugar": 40, "Milk": 30, "Eggs": 5}
quantities = {"Rice": 2, "Sugar": 1, "Milk": 3, "Eggs": 12}

total_bill = sum(prices[item] * quantities.get(item, 0) for item in prices)

print("Total bill:", total_bill)
