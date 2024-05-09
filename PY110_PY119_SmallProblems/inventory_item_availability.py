'''Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item is available. As before, the function takes two arguments: an inventory item and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.'''

import inventory_item_transactions

def is_item_available(item_id, transactions):
    item_transactions = inventory_item_transactions.transactions_for(item_id, transactions)
    item_quantity = sum([transaction['quantity'] if transaction['movement'] == 'in' else -transaction['quantity'] for transaction in item_transactions])
    return item_quantity > 0

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True