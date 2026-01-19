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
# Each item is stored as a tuple: (item_name, price)
# -----------------------------
my_cart = []

# -----------------------------
# Main menu loop
# Keeps running until user chooses checkout or end
# -----------------------------
while True:

    # Show menu options to the user
    print('\nHow would you like to proceed')
    print('add item')
    print('view cart')
    print('checkout')
    print('end')

    # Read user choice
    user_action = input('enter your choice: ')

    # -------------------------
    # Add item logic
    # -------------------------
    if user_action == 'add item':
        # Display available items
        print('\nAvailable items:')
        for key, value in display_items.items():
            print(f'{key}: {value}')

        # Ask which item to add
        chosen_item = input('Which item would you like to add? ')

        # Check if item exists in catalog
        if chosen_item in display_items:
            price = display_items[chosen_item]
            my_cart.append((chosen_item, price))
            print(f'{chosen_item} added to cart')
        else:
            print('Item not found')

    # -------------------------
    # View cart logic
    # -------------------------
    if user_action == 'view cart':
        # Check if cart is empty
        if not my_cart:
            print('Your cart is empty')
        else:
            total = 0
            print('\nYour cart items:')
            for item, price in my_cart:
                print(f'{item}: {price}')
                total += price

            # Display total price
            print(f'\nTotal amount: {total}')

    # -------------------------
    # Exit conditions
    # -------------------------
    if user_action == 'checkout' or user_action == 'end':
        print('Thank you!')
        break
