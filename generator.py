from models import Trial
from rules import compute_expected_answer
from string import ascii_uppercase
import random

def generate_trial(rng: random.Random) -> Trial:
    position = rng.choice(['TOP', 'BOTTOM'])
    letter = rng.choice(ascii_uppercase) # utilizziamo ascii_uppercase perché contiene le lettere dell'alfabeto
    number = rng.randint(1, 9)
    expected_answer = compute_expected_answer(position, letter, number)

    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=expected_answer
    )
