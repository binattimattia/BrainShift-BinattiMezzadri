def is_even(number: int) -> bool:
    """
    Controlla se un numero è pari
    
    Args:
        number: Il numero da controllare
    
    Returns:
        True se il numero è pari, False altrimenti
    """
    try:
        return number % 2 == 0
    except (TypeError, ValueError) as e:
        raise ValueError(f"The character is not a number")

def is_vowel(letter: str) -> bool:
    """
    Controlla se un carattere è una vocale
    
    Args:
        letter: Il carattere da controllare
    
    Returns:
        True se il carattere è una vocale, False altrimenti
    """
    try:
        return letter.lower() in ["a", "e", "i", "o", "u"]
    except (TypeError, ValueError) as e:
        raise ValueError(f"The character is not a letter")

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    """
    Calcola la risposta attesa in base alla posizione, alla lettera e al numero
    
    Args:
        position: La posizione della carta
        letter: La lettera della carta
        number: Il numero della carta
    
    Returns:
        La risposta attesa
    """
    try:
        if position.lower() == "top":
            return is_even(number)
        elif position.lower() == "bottom":
            return is_vowel(letter)
        else:
            raise ValueError(f"Invalid position: {position}")
    except (AttributeError, TypeError) as e:
        raise ValueError(f"The characters are incompatible: {e}")
