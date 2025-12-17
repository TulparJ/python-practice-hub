# Today's Mongolia Python
# Topic: Hash Map + String

def name_frequency(names):
    freq = {}
    for n in names:
        freq[n] = freq.get(n, 0) + 1
    return freq

def first_unique_name(names):
    freq = name_frequency(names)
    for n in names:
        if freq[n] == 1:
            return n
    return None


if __name__ == "__main__":
    names = [
        "Bat", "Bold", "Temuulen",
        "Bat", "Naran", "Bold"
    ]

    print("Name frequency:", name_frequency(names))
    print("First unique name:", first_unique_name(names))
