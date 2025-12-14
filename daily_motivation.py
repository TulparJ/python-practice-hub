import random
from datetime import date

motivations = [
    "You got this 💪",
    "Small steps still move you forward.",
    "Focus on progress, not perfection.",
    "Your future self will thank you.",
    "Discipline beats motivation every time."
]

tips = [
    "Take a 5-minute break.",
    "Write down your top 3 goals for today.",
    "Drink some water.",
    "Clean your desk for 2 minutes.",
    "Put your phone away while working."
]

def daily_motivation():
    today = date.today().strftime("%B %d, %Y")
    msg = random.choice(motivations)
    tip = random.choice(tips)

    print(f"📅 Today: {today}")
    print(f"✨ Motivation: {msg}")
    print(f"💡 Tip: {tip}")


if __name__ == "__main__":
    daily_motivation()
