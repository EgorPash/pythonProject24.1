import stripe
from django.conf import settings
from materials.models import Payment

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def create_product(name, description):
    product = stripe.Product.create(name=name, description=description)
    return product

def create_price(product_id, amount):
    price = stripe.Price.create(
        unit_amount=int(amount * 100),  # Переводим в копейки
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
        success_url='https://your-domain/success/',
        cancel_url='https://your-domain/cancel/',
    )
    return session