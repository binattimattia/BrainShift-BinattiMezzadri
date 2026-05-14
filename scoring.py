from config import POINTS_CORRECT, POINTS_WRONG

def apply_answer(score: int, is_correct: bool) -> int:
    """
    Applica il punteggio in base alla risposta data
    
    Args:
        score: Il punteggio corrente
        is_correct: Se la risposta è corretta
    
    Returns:
        Il nuovo punteggio
    """
    new_score = score + POINTS_CORRECT if is_correct else score - POINTS_WRONG
    return max(0, new_score)
