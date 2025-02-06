import art
print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
should_continue = True
bidding_dictionary = {}
while should_continue:
    name = input("What's your name?:  ")
    bid = int(input("What's your bid?:  $"))
    bidding_dictionary[name] = bid
    bidders = input("Are there any other bidders? Type 'yes' or 'no':  ").lower()
    if bidders == "no":
        should_continue = False
    else:
        print("\n" * 20)
max = 0
winner = ""
for key in bidding_dictionary:
    if bidding_dictionary[key] > max:
        max = bidding_dictionary[key]
        winner = key

print(f"The winner is {winner} with a bid of ${max}!")

