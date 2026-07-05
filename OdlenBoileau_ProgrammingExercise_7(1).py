# Import the csv module

import csv

#Programming Exercise 7

# Function to create the grades.csv file

def create_grades_file():

    # Ask the user how many students they want to enter

    num_students = int(input("How many students do you want to enter? "))

    # Open grades.csv in write mode

    with open("grades.csv", "w", newline="") as file:

        # Create a csv writer object

        writer = csv.writer(file)

        # Write the column headings

        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student

        for i in range(num_students):

            # Display the current student number

            print(f"\nStudent {i + 1}")

            # Get the student's first name

            first_name = input("First Name: ")

            # Get the student's last name

            last_name = input("Last Name: ")

            # Get the student's first exam grade

            exam1 = int(input("Exam 1 Grade: "))

            # Get the student's second exam grade

            exam2 = int(input("Exam 2 Grade: "))

            # Get the student's third exam grade

            exam3 = int(input("Exam 3 Grade: "))

            # Write the student's information to the CSV file

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Display a confirmation message

    print("\ngrades.csv has been created successfully.")

# Call the function

create_grades_file()

