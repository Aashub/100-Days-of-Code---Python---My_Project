from art import  logo
print(logo)

def find_highest_bidder(dictionary):
    highest_bidder = 0
    highest_bidder_name = ""

    # this for loop will determine that who has bided the most amount and store their details in above variables
    for bid in dictionary:

        if highest_bidder < dictionary[bid]:
            highest_bidder = dictionary[bid]
            highest_bidder_name = bid

    print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder}")


# this dictionary will store the bidder name and each bidder amount
bidding_dictionary = {}

should_continue = True

# this while loop will run until its condition doesn't become false
while should_continue:

    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    other_bidder = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    # here we are adding all bidder name as "Key" and bid_amount as each key value
    bidding_dictionary[bidder_name] = bid_amount

    if other_bidder == "yes":
        pass
        print("\n" * 20)

    # this condition will run if all the bidder has bided their amount
    elif other_bidder == "no":

        find_highest_bidder(bidding_dictionary)
        should_continue = False







