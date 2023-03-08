from shorturl import settings

from random import choice

from string import ascii_letters, digits

MAX_LENGTH = 7

POSSIBLE_CHARS = ascii_letters + digits

def create_code(chars=POSSIBLE_CHARS):

    return "".join(
        [choice(chars) for _ in MAX_LENGTH]
    )


def create_short_url(model_instance):

    code = create_code()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_one=code).exists():
        
        return create_short_url(model_instance)
    
    return code
