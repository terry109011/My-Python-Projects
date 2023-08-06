# Project 28 - Blind Auction

from ascii_art import logo
import os

global bidders

print(logo)

bidders_dict = {}
end_auction = False
while not end_auction:
    bidder_name = input('What is your name? ').capitalize()
    
    # Input must be an integer
    while True:
        try:
            bid_amount = int(input('What is your bid amount? '))
            bidders_dict.update({bidder_name : bid_amount})
            break
        except ValueError or TypeError:
            print('Numeric input only.')
            continue
    
    next_bid = input('Are there any other bidder (Y/N)? : ')
    
    option = ['Y','y','N','n']
    while next_bid not in option:
        next_bid = input('Are there any other bidder (Y/N)? : ')
        
    if next_bid == option[0] or next_bid == option[1]:
        os.system('cls')
        continue
    else:
        # return bidder with max value
        bidder_list = list(bidders_dict.keys())
        amount_list = list(bidders_dict.values())
        highest_amount = max(amount_list)
        highest_bidder = bidder_list[amount_list.index(highest_amount)]
        print(f'The winner is {highest_bidder} with a bid of ${highest_amount}.')
        end_auction = True
    
        
        
        
        
