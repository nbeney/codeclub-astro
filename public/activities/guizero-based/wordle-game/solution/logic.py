COLOR_CORRECT = "green"
COLOR_MISPLACED = "yellow"
COLOR_WRONG = "darkgrey"


def compare_words(guess, word):
    """Compare the guess to the word and return a list of colors to display."""

    colors = [COLOR_WRONG] * len(guess)
    used = [False] * len(guess)

    # First pass: mark all the correct letters.
    for idx in range(len(guess)):
        if guess[idx] == word[idx]:
            colors[idx] = COLOR_CORRECT
            used[idx] = True

    # Second pass: mark all the misplaced letters.
    for idx_guess in range(len(guess)):
        if colors[idx_guess] == COLOR_CORRECT:
            continue
        for idx_word in range(len(word)):
            if guess[idx_guess] == word[idx_word] and not used[idx_word]:
                colors[idx_guess] = COLOR_MISPLACED
                used[idx_word] = True
                break

    return colors
