import random
import string
from shortener.models import Link

def random_hash_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_hash_generator():
    hash = random_hash_generator()
    if not len(Link.objects.filter(hash=hash)) > 0:
        return hash
    return unique_hash_generator()
