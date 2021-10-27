import random


# For credit for this function, see README
def generate_sku():
    """
    Generate SKU for each new product
    """
    return str(random.randint(1000000000, 9999999999))
