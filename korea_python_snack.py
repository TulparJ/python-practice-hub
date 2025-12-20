# Korea Python Project
# Theme: Korean Street Snack Prices 🍢
# Topic: Lists + Min/Max/Average

def average_price(prices):
    return sum(prices) / len(prices)

def most_expensive(prices, items):
    max_price = max(prices)
    idx = prices.index(max_price)
    return items[idx], max_price

def cheapest(prices, items):
    min_price = min(prices)
    idx = prices.index(min_price)
    return items[idx], min_price

if __name__ == "__main__":
    snacks = ["Tteokbokki", "Hotteok", "Gimbap", "Odeng"]
    prices = [3000, 2500, 2000, 1500]  # in KRW

    print("Average price:", average_price(prices), "KRW")
    expensive = most_expensive(prices, snacks)
    print("Most expensive snack:", expensive[0], "-", expensive[1], "KRW")
    cheap = cheapest(prices, snacks)
    print("Cheapest snack:", cheap[0], "-", cheap[1], "KRW")
