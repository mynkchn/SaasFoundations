# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from decouple import config
stripe.api_key = config('STRIPE_API_KEY',cast=str,default=None)

stripe.Customer.create(
  name="Jenny Rosen",
  email="jennyrosen@example.com",
)