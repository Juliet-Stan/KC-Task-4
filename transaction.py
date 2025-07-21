import datetime

class Transaction:
    def __init__(self, category, amount):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.date}, {self.category}, ${self.amount:.2f}"






