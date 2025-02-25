# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_tR3PYbcVNZZ796tH88S4VQ2u"

stripe.Customer.create(
  name="Jenny Rosen",
  email="jennyrosen@example.com",
)