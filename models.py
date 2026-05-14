from dataclasses import dataclass

@dataclass
class Trial:
    """
    Rappresenta una singola prova del gioco
    """
    position: str
    letter: str
    number: int
    expected_answer: bool
    is_correct: bool = None
    user_answer: bool | None = None
    