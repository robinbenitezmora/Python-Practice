# A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?

data = [1, 2, 3, 2, 4, 3]
unique_data = list(set(data))
order_data = sorted(unique_data)
print(order_data)  # The order is not guaranteed to be [1, 2, 3, 4]
