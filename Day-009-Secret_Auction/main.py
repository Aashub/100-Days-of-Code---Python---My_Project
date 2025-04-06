from art import logo

print(logo)

#empty dictionary to store the name and bid values
biding_details = {}

#This function will give us the highest bidder who won the bid.
def Blind_Auction():
    name = input("What is your Name?: ").lower()
    bid = int(input("What is your bid?: $"))

    # here the bidder name and their bid is being added in the dictionary
    biding_details[name] = bid

    should_continue = True
    while should_continue:
        other_bidders = input("Are there any other bidders? Type 'Yes' or 'no'.").lower()

        # if There is another bidder then this if statement will run the blind_auction function run again so the next
        # bidder bid their amount
        if other_bidders == "yes":
            print("\n" * 15)
            Blind_Auction()

        #if their no other bidder then this elif statement will run and give us the highest bidder.
        elif other_bidders == "no":
            highest_bidder = 0
            bidder_name = ""

            # here the highest bidder we are going to be found out.
            for bid in biding_details:

                if biding_details[bid] >= highest_bidder:
                    highest_bidder = biding_details[bid]
                    bidder_name = bid

            print(f"\nThe winner is {bidder_name} with a bid of ${highest_bidder}")
            exit()

        else:
            print("Input is Wrong!, Please provide the correct input!")

Blind_Auction()




