import random

def code_generator(size=6, chars='abcdtyuiopf'):
    return ''.join(random.choice(chars) for _ in range (size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.object.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code