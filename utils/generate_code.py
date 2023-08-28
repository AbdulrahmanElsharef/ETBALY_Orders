import random


def generate_code(n=9):
    numbers = '123456789'
    code = ''.join(random.choice(numbers) for x in range(n))
    return f'01{code}'

def generate_sku(n=9):
    numbers = '123456789'
    code = ''.join(random.choice(numbers) for x in range(n))
    return f'sku{code}'


# print(f'{slugify("web design")}-category-{generate_code()[:4]}')