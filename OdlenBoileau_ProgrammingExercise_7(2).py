# Import the csv module

import csv

# Function to read and display the grades.csv file

def display_grades():

    # Open grades.csv in read mode

    with open("grades.csv", "r") as file:

        # Create a csv reader object

        reader = csv.reader(file)

        # Loop through each row in the file

        for row in reader:

            # Display the data in a table format

            print("{:<15}{:<15}{:<10}{:<10}{:<10}".format(*row))

# Call the function

display_grades()