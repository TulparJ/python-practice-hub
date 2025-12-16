# Mongolia Python Project
# Topic: Hash Map + Strings

def city_frequency(cities):
    freq = {}
    for city in cities:
        freq[city] = freq.get(city, 0) + 1
    return freq


def longest_city_name(cities):
    longest = cities[0]
    for city in cities:
        if len(city) > len(longest):
            longest = city
    return longest


if __name__ == "__main__":
    cities = [
        "Ulaanbaatar", "Darkhan", "Erdenet",
        "Ulaanbaatar", "Choibalsan", "Darkhan",
        "Ulaanbaatar"
    ]

    print("City frequency:", city_frequency(cities))
    print("Longest city name:", longest_city_name(cities))
