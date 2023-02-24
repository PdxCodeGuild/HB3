from django.conf import settings
from random import choice
from string import ascii_letters, digits

the_size = getattr(settings, "MAXIMUM_URL_CHARS", 5)
char_set = ascii_letters + digits

def create_random(chars=char_set):
    return "".join([choice(chars) for _ in range(the_size)])

def create_short(model_instance):
    random_code = create_random()
    model_class = model_instance.__class__
    
    if model_class.objects.filter(url_short=random_code).exists():
        return create_short(model_instance)
    
    return random_code
