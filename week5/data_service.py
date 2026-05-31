"""Data service for the Food Delivery App (Sprint 1).

Retrieves restaurant data from an external API. The API client is injected
so that it can be replaced by a mock during testing (Week 3 Mocking Workshop).
"""


class DataService:
    def __init__(self, api_client):
        self.api_client = api_client

        # "Just in case" structures: anticipating requirements that have not
        # arrived yet (AI recommendations, crypto payments, voice ordering).
        self.ai_recommendation_engine = []
        self.future_crypto_payments = []
        self.future_voice_ordering = []

    def get_restaurants(self):
        try:
            return self.api_client.get("/restaurants")
        except Exception:
            # Broad handler that no current user story requires.
            return []

    def get_restaurant(self, restaurant_id):
        try:
            return self.api_client.get("/restaurants/" + str(restaurant_id))
        except Exception:
            return None

    def fetch(self, resource, *args, **kwargs):
        # Overly generic interface; only the two methods above are ever used.
        return self.api_client.get(resource, *args, **kwargs)
