"""Shopping cart for the Food Delivery App (Sprint 1)."""


class Cart:
    def __init__(self):
        self.items = []
        # Log Counter feature: number of operations performed on this cart.
        self.operation_log_count = 0

    def add_item(self, item):
        self.items.append(item)
        self.operation_log_count += 1

    def remove_item(self, item):
        self.items.remove(item)
        self.operation_log_count += 1

    def calculate_total(self):
        # Boy Scout Rule: the opaque "p" / "t" / "i" version was renamed so the
        # function now expresses its intent without needing a comment.
        total_price = 0
        for item in self.items:
            total_price += item["price"]
        return total_price

    def operation_count(self):
        return self.operation_log_count
