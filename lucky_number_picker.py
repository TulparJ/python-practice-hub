import random

def lucky_number():
    num = random.randint(1, 99)
    messages = [
        "Today’s your day.",
        "Big energy incoming.",
        "Stay locked in.",
        "Trust the grind.",
        "Good things brewing."
    ]
    return num, random.choice(messages)

if __name__ == "__main__":
    num, msg = lucky_number()
    print("Your lucky number:", num)
    print("Message:", msg)
