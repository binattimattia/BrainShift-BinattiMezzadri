from dataclasses import dataclass

@dataclass
class Trial:
    is_correct: bool = False
    user_answer: bool | None = None
    