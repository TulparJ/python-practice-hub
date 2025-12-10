import random

def flip():
    return random.choice(["Heads", "Tails"])

if __name__ == "__main__":
    print("Coin Flip Simulator 🪙")

    while True:
        input("Press Enter to flip the coin...")
        print("Result:", flip())

        again = input("Flip again? (y/n): ").lower()
        if again != 'y':
            print("Aight bet, see you next flip 😎")
            break
