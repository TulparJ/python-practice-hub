# Mongolia Python Project
# Theme: Naadam Festival Results
# Topic: Dictionary + Sorting

def sort_wrestlers(results):
    # results: {name: wins}
    return sorted(results.items(), key=lambda x: x[1], reverse=True)


def champion(results):
    ranked = sort_wrestlers(results)
    return ranked[0]


if __name__ == "__main__":
    wrestlers = {
        "Bat-Erdene": 7,
        "Sumiyabazar": 9,
        "Ganzorig": 6,
        "Khurelbaatar": 8
    }

    ranking = sort_wrestlers(wrestlers)
    print("Naadam Wrestling Ranking:")
    for name, wins in ranking:
        print(f"{name}: {wins} wins")

    champ = champion(wrestlers)
    print("\nChampion:", champ[0])
