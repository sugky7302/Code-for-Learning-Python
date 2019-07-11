def apply_discount(product, discount):
    price = int(product['price']) * (1.0 - discount)
    assert 0 <= price <= product['price']
    return price


product = {
    'price': 250,
}

print(apply_discount(product, 0.6))
print(apply_discount(product, 1.01))