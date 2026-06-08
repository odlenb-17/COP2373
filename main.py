
# Display the number of tickets remaining after each successful purchase.



def show_remaining(tickets_left):



    print("Tickets remaining:", tickets_left)



# Manage ticket sales by validating purchases, updating inventory,



# and tracking the total number of buyers.



def sell_tickets():



    # Store the starting number of tickets available for sale.



    TOTAL_TICKETS = 20



    # Initialize the number of tickets currently available.



    tickets_left = TOTAL_TICKETS



    # Track the number of successful buyers throughout the program.



    buyers = 0



    # Continue accepting purchases until all tickets have been sold.



    while tickets_left > 0:



        # Display the current number of tickets available before purchase.



        print("\nTickets available:", tickets_left)



        # Ask the user how many tickets they would like to purchase.



        tickets = int(input("How many tickets would you like to buy (1-4)? "))



        # Ensure the requested number of tickets is within the allowed range.



        if tickets < 1 or tickets > 4:



            print("You can only buy between 1 and 4 tickets.")



        # Prevent users from purchasing more tickets than remain.



        elif tickets > tickets_left:



            print("Not enough tickets available.")



        else:



            # Subtract the purchased tickets from the remaining inventory.



            tickets_left -= tickets



            # Increase the buyer count after a successful purchase.



            buyers += 1



            # Show the updated number of tickets remaining.



            show_remaining(tickets_left)



    # Inform the user when all tickets have been sold.



    print("\nAll tickets have been sold!")



    # Display the total number of buyers who purchased tickets.



    print("Total number of buyers:", buyers)



# Begin the ticket-selling process by calling the main function.



sell_tickets()
