def group_by_category(transactions):
    transactions_by_category = {}
    for transaction in transactions:
        if transaction.category in transactions_by_category:
            transactions_by_category[transaction.category].append(transaction)
        else:
            transactions_by_category[transaction.category] = [transaction]
    return transactions_by_category

def calculate_totals(transactions_by_category):
    totals = {}
    for category, transactions in transactions_by_category.items():
        total = sum(transaction.amount for transaction in transactions)
        totals[category] = total
    return totals
