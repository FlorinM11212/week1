"""Data service for the Food Delivery App (Sprint 1).

Retrieves restaurant data from an external API. The API client is injected
so that it can be replaced by a mock during testing (Week 3 Mocking Workshop).
"""

# AUDIT NOTE
# The previous version carried "just in case" attributes and an overly generic
# interface that no Sprint 1 user story required:
#   # MUDA: Needless Complexity -> self.ai_recommendation_engine
#   # MUDA: Needless Complexity -> self.future_crypto_payments
#   # MUDA: Needless Complexity -> self.future_voice_ordering
#   # MUDA: Needless Complexity -> generic fetch(resource, *args, **kwargs)
#   # MUDA: Needless Complexity -> broad "except Exception" handlers
# All of the above have been removed. Only behaviour backed by a current user
# story (browse restaurants) remains.


class DataService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_restaurants(self):
        return self.api_client.get("/restaurants")

    def get_restaurant(self, restaurant_id):
        return self.api_client.get("/restaurants/" + str(restaurant_id))
