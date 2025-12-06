# Mongolian Zodiac Finder

animals = [
    "Хулгана", "Үхэр", "Бар", "Туулай",
    "Луу", "Могой", "Морь", "Хонь",
    "Бич", "Тахиа", "Нохой", "Гахай"
]

year = int(input("Төрсөн жилээ оруулна уу: "))

index = (year - 4) % 12  # Zodiac cycle starts at 4 AD

print(f"Таны жил: {animals[index]}")
