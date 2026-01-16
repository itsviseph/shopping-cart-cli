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
for key, value in display_items.items():
    print(f'{key}: {value}')

# -----------------------------
# Main menu loop
# Repeats until user chooses checkout or end
# -----------------------------
while True:

    # Display menu options
    print('How would you like to proceed')
    print('add item')
    print('view cart')
    print('checkout')
    print('end')

    # Get user action
    user_action = input('enter your choice: ')

    # -------------------------
    # Planned feature: Add item
    # -------------------------
    # if user_action == 'add item':
        # show items again
        # ask which item to add
        # add selected item to cart
        # continue loop

    # -------------------------
    # Planned feature: View cart
    # -------------------------
    # if user_action == 'view cart':
        # display items in cart
        # display individual prices
        # calculate total cart value
        # display total
        # continue loop

    # -------------------------
    # Exit conditions
    # -------------------------
    if user_action == 'checkout' or user_action == 'end':
        print('Thank you!')
        break
