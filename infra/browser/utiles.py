import string
import random


def generate_random_string(length):
    """
          generates a random letters string for a given length
          """
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string
