"""Shopping cart for the Food Delivery App (Sprint 1)."""


class Cart:
    def __init__(self):
        self.items = []

        # Gold-plating: placeholders for features that are not in Sprint 1.
        self.ai_recommendation_engine = []
        self.future_crypto_payments = []
        self.future_voice_ordering = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def p(self, x):
        t = 0
        for i in x:
            t += i["price"]
        return t
