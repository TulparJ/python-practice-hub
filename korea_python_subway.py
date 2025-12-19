# Korea Python Project
# Theme: Seoul Subway Rush Hours 🚇
# Topic: Lists + Conditionals

def peak_hours(rides):
    peak = 0
    off_peak = 0

    for hour in rides:
        if 7 <= hour <= 9 or 17 <= hour <= 19:
            peak += 1
        else:
            off_peak += 1

    return peak, off_peak


if __name__ == "__main__":
    # ride times (hour of day)
    ride_times = [6, 7, 8, 10, 12, 18, 19, 21]

    peak, off_peak = peak_hours(ride_times)
    print("Peak hour rides:", peak)
    print("Off-peak rides:", off_peak)
