"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    current_cart = { item: notes.count(item) for item in notes}

    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    recipe_updates = dict(recipe_updates)
    final = ideas | recipe_updates
    return final


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for key in cart.keys():
        fulfillment_cart[key] = [cart[key]] + aisle_mapping[key]
    return dict(sorted(fulfillment_cart.items(), reverse=True))



def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    newd = dict()

    # Reduce the number of item from inventory
    for key, values in fulfillment_cart.items():
        store_inventory[key][0] = store_inventory[key][0] - values[0]
        if store_inventory[key][0] == 0:
            store_inventory[key][0] = 'Out of Stock'
    return store_inventory
    # Replace the number for Out of stock if goes down to 0
