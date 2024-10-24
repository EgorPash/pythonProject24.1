import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def create_product(name):
    product = stripe.Product.create(name=name)
    return product

def create_price(product_id, amount):
    price = stripe.Price.create(
        unit_amount=amount * 100,  # В Stripe сумма в копейках
        currency='usd',
        product=product_id,
    )
    return price

def create_checkout_session(price_id):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
    )
    return session