# Korea Python Project
# Theme: Korean Café Orders ☕
# Topic: Lists + Sum/Average

def total_price(prices):
    return sum(prices)

def average_price(prices):
    return sum(prices) / len(prices)

if __name__ == "__main__":
    orders = ["Americano", "Latte", "Cake", "Mocha"]
    prices = [4500, 5000, 7000, 5500]  # KRW

    print("Total order price:", total_price(prices), "KRW")
    print("Average price per item:", average_price(prices), "KRW")
