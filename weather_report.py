import random

temps = [ -15, -10, -5, 0, 5, 10, 15 ]
conditions = ["Sunny", "Cloudy", "Snowing", "Windy"]

print("=== Ulaanbaatar Weather Report ===")
print("Temperature:", random.choice(temps), "°C")
print("Condition:", random.choice(conditions))
