# -----------------------------
# Product catalog (item -> price)
# -----------------------------
display_items = {
    'macbook': 1000,
    'iphone': 900,
    'watch': 700,
    'ipad': 800
}

# -----------------------------
# Cart to store selected items
# -----------------------------
my_cart = []


def view_items():
    print('\nAvailable items:')
    for key, value in display_items.items():
        print(f'{key}: {value}')


def add_item():
    view_items()
    chosen_item = input('Which item would you like to add? ')

    # Check if item exists in catalog
    if chosen_item in display_items:
        price = display_items[chosen_item]
        my_cart.append((chosen_item, price))
        print(f'{chosen_item} added to cart')
    else:
        print('Item not found')


def view_cart():
    if not my_cart:
        print('Your cart is empty')
        return

    total = 0
    print('\nYour cart items:')
    for item, price in my_cart:
        print(f'{item}: {price}')
        total += price

    print(f'\nTotal amount: {total}')


while True:
    print('\nHow would you like to proceed')
    print('add item')
    print('view cart')
    print('checkout')
    print('end')

    user_action = input('enter your choice: ')

    if user_action == 'add item':
        add_item()

    elif user_action == 'view cart':
        view_cart()

    elif user_action == 'checkout':
        view_cart()
        print('Thank you!')
        break

    elif user_action == 'end':
        print('Thank you!')
        break

    else:
        print('Invalid input, please try again')
