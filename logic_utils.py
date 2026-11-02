def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess within [low, high].

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIXME: fixed bug 3 - decimals were silently truncated (int(float(raw))) and there was
    # no range check, so 500 or -5 were accepted and used up an attempt. Only whole numbers
    # inside the difficulty range are valid now.
    # Collaboration: I reproduced 500 / -5 / 2.7 in the app and logged it; the AI proposed
    # moving parse_guess here with low/high parameters, and I reviewed it and added tests.
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    raw = raw.strip()
    try:
        value = int(raw)
    except ValueError:
        try:
            float(raw)
        except ValueError:
            return False, None, "That is not a number."
        return False, None, "Enter a whole number, not a decimal."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIXME: fixed bug 1 - hint messages were swapped, and a str(secret) fallback
    # caused string comparison ("9" > "40"). Both ints are compared numerically now.
    # Collaboration: I spotted the swapped hints while playing; the AI traced the str(secret)
    # fallback as the root cause, then I reviewed its fix and verified it with pytest.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
