# Today's Japan Python Project
# Theme: Sushi Order Stats 🍣
# Topic: Hash Map

def sushi_frequency(orders):
    freq = {}
    for item in orders:
        freq[item] = freq.get(item, 0) + 1
    return freq


def most_popular_sushi(orders):
    freq = sushi_frequency(orders)
    popular = None
    max_count = 0

    for sushi, count in freq.items():
        if count > max_count:
            max_count = count
            popular = sushi

    return popular, max_count


if __name__ == "__main__":
    orders = [
        "Salmon", "Tuna", "Eel",
        "Salmon", "Salmon", "Tuna",
        "Shrimp"
    ]

    print("Sushi frequency:", sushi_frequency(orders))
    popular = most_popular_sushi(orders)
    print("Most popular sushi:", popular[0], "-", popular[1], "orders")
