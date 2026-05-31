"""Shopping cart for the Food Delivery App (Sprint 1)."""

# AUDIT NOTE
# The previous version anticipated features that are not part of Sprint 1:
#   # MUDA: Needless Complexity -> self.ai_recommendation_engine
#   # MUDA: Needless Complexity -> self.future_crypto_payments
#   # MUDA: Needless Complexity -> self.future_voice_ordering
# These placeholders have been removed. The cart now stores only what the
# current user story needs: the list of items added by the customer.


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def p(self, x):
        t = 0
        for i in x:
            t += i["price"]
        return t
