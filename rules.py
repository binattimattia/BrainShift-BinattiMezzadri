def is_even(number: int) -> bool:
    try:
        return number % 2 == 0
    except (TypeError, ValueError) as e:
        raise ValueError(f"The character is not a number")

def is_vowel(letter: str) -> bool:
    try:
        return letter.lower() in ["a", "e", "i", "o", "u"]
    except (TypeError, ValueError) as e:
        raise ValueError(f"The character is not a letter")

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    try:
        if position.lower() == "top":
            return is_even(number)
        elif position.lower() == "bottom":
            return is_vowel(letter)
        else:
            raise ValueError(f"Invalid position: {position}")
    except (AttributeError, TypeError) as e:
        raise ValueError(f"The characters are incompatible: {e}")
