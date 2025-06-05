    import stripe
    from django.conf import settings

    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    def create_payment(amount, currency='usd'):
        return stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
        )
    