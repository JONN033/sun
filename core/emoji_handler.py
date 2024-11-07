import random
from core.file_loader import load_emojis

def get_random_emoji():
    emojis = load_emojis()
    return random.choice(emojis) if emojis else None
