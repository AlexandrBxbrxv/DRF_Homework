import stripe

from config.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY


def create_stripe_session(obj):
    """Создает сессию на оплату в страйпе."""
    product_name = obj.paid_course.title if obj.paid_course.title else ''

    product = stripe.Product.create(
        name=product_name
    )

    price = stripe.Price.create(
        currency="rub",
        unit_amount=obj.payment_amount * 100,
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": f'{price.id}', "quantity": 1}],
        mode="payment",
    )

    return session.get('id'), session.get('url')
