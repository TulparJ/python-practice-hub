# Today's Volleyball Python
# Topic: Dictionary + Max

def serve_speed_stats(players):
    fastest_player = None
    max_speed = 0

    for name, speed in players.items():
        if speed > max_speed:
            max_speed = speed
            fastest_player = name

    return fastest_player, max_speed


def average_speed(players):
    total = 0
    for speed in players.values():
        total += speed
    return total / len(players)


if __name__ == "__main__":
    # jump serve speeds (km/h)
    serve_speeds = {
        "Tulpar": 92,
        "Bat-Erdene": 88,
        "Temuulen": 90,
        "Bold": 85
    }

    fastest = serve_speed_stats(serve_speeds)
    print("Fastest jump serve:", fastest[0], "-", fastest[1], "km/h")
    print("Average serve speed:", average_speed(serve_speeds), "km/h")
