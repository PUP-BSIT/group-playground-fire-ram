transactions = [{'transaction_id': 'T001', 'customer_id': 'C001', 'amount': 150},
                {'transaction_id': 'T002', 'customer_id': 'C002', 'amount': 250},
                {'transaction_id': 'T003', 'customer_id': 'C001', 'amount': 300},
                {'transaction_id': 'T004', 'customer_id': 'C003', 'amount': 100}
]

for transaction in transactions:
    if transaction['amount'] > 200:
        print(f" {transaction['transaction_id']} {transaction['amount']}")  