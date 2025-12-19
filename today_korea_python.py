# Today's Korea Python Project
# Theme: K-pop Song Popularity 🎵
# Topic: Hash Map

def song_frequency(plays):
    freq = {}
    for song in plays:
        freq[song] = freq.get(song, 0) + 1
    return freq


def most_played_song(plays):
    freq = song_frequency(plays)
    top_song = None
    max_plays = 0

    for song, count in freq.items():
        if count > max_plays:
            max_plays = count
            top_song = song

    return top_song, max_plays


if __name__ == "__main__":
    plays = [
        "IU - Love Poem", "BTS - Spring Day", "NewJeans - Hype Boy",
        "BTS - Spring Day", "IU - Love Poem",
        "BTS - Spring Day"
    ]

    print("Song frequency:", song_frequency(plays))
    top = most_played_song(plays)
    print("Most played song:", top[0], "-", top[1], "plays")
