import random


def generate_sku():
    """
    Generate SKU for each new product
    """
    return str(random.randint(1000000000, 9999999999))
