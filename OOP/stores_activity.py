def sale(store,item,sales):
    for store_item in store.items:
        if item.name == store_item.name:
            store_item.qty -= 1
            sales += store_item.price
    return sales

def sale_returns(store,item,sales):
    for store_item in store.items:
        if item.name == store_item.name:
            store_item.qty -= 1
            sales -= store_item.price
    return sales

"""
Make a class Store with attributes:
items - list of items
sales

Make a class Item with attributes:
name
qty - quanity
price

Create 2 Stores
Store A should have sold 2 items and 1 item returned
Store B have sold 1 item and 0 return
"""
