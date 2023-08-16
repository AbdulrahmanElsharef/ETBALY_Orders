import random


def generate_code(n=3):
    numbers = '12345'
    code = ''.join(random.choice(numbers) for x in range(n))
    return f'Order-00{code}'


# print(f'{slugify("web design")}-category-{generate_code()[:4]}')