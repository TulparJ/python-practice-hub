text = input("Enter text: ").lower()
vowels = "aeiou"
count = sum(1 for c in text if c in vowels)
print("Vowel count:", count)
