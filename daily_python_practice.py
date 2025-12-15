# Daily Python Practice
# Topic: Hash Map + String

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    return freq

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


if __name__ == "__main__":
    text = "data structures"
    print("Character frequency:", char_frequency(text))

    word = "level"
    print(f"Is '{word}' a palindrome?", is_palindrome(word))
