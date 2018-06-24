def get_freq_score(message):
    """
    Evaluates the given message according to its character frequency.
    The higher the score, the likelier it is for the text to be human-readable.
    """

    score = 0
    common_letters = 'etaoin shrdlu'
    for c in message:
        if c in common_letters:
            score += 3
        else:
            score -= 1
    return score
