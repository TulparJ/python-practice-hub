from datetime import datetime

def log_mood():
    mood = input("How are you feeling today? ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"{now} - Mood: {mood}\n"
    
    with open("mood_log.txt", "a") as file:
        file.write(entry)

    print("Your mood has been logged. Stay strong king 👑")

log_mood()
