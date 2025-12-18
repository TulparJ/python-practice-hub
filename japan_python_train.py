# Japan Python Project
# Theme: Tokyo Train Punctuality 🚆
# Topic: List + Conditionals

def average_delay(delays):
    total = 0
    for d in delays:
        total += d
    return total / len(delays)


def delay_status(delay):
    if delay == 0:
        return "On time"
    elif delay <= 2:
        return "Minor delay"
    else:
        return "Apology announcement required 😅"


if __name__ == "__main__":
    # delays in minutes
    train_delays = [0, 1, 0, 2, 0, 0, 3]

    avg = average_delay(train_delays)
    print("Average delay:", avg, "minutes")

    today = 3
    print("Today's status:", delay_status(today))
