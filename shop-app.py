# -----------------------------
# Product catalog (item -> price)
# -----------------------------

display_items = {
    'macbook': 1000,
    'iphone': 900,
    'watch': 700,
    'ipad': 800
}

# Display available items and prices (runs once)


# Cart to store selected items
my_cart = []

# -----------------------------
# Main menu loop
# Repeats until user chooses checkout or end
# -----------------------------
while True:

    # Display menu options
    print('\nHow would you like to proceed')
    print('add item')
    print('view cart')
    print('checkout')
    print('end')

    # Get user action
    user_action = input('enter your choice: ')

    # -------------------------
    # Add item logic
    # -------------------------
    if user_action == 'add item':
        print('\nAvailable items:')
        for key, value in display_items.items():
            print(f'{key}: {value}')

        chosen_item = input('Which item would you like to add? ')

        if chosen_item in display_items:
            price = display_items[chosen_item]
            my_cart.append((chosen_item, price))
            print(f'{chosen_item} added to cart')
        else:
            print('Item not found')

    if user_action == 'view cart':
        if not my_cart:
            print('Your cart is empty')
        else:
            for item, price in my_cart:
                print(f'{item}: {price}')

    # -------------------------
    # View cart logic (planned)
    # -------------------------
    # if user_action == 'view cart':
    #     pass

    # -------------------------
    # Exit conditions
    # -------------------------
    if user_action == 'checkout' or user_action == 'end':
        print('Thank you!')
        break

