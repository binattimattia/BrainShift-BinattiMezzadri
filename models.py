from dataclasses import dataclass

@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool
    is_correct: bool = False
    user_answer: bool | None = None
    