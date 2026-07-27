# Import the NumPy library

import numpy as np

# Function to load grades from the CSV file

def load_grades(filename):

    # Read only the exam score columns (Exam 1, Exam 2, Exam 3)

    # Skip the header row

    grades = np.loadtxt(filename,

                        delimiter=",",

                        skiprows=1,

                        usecols=(2, 3, 4))

    # Return the NumPy array

    return grades

# Function to calculate and display statistics

def display_statistics(grades):

    # Display the first five rows of the dataset

    print("First Five Rows:")

    print(grades[:5])

    # Display statistics for each exam

    print("\nStatistics for Each Exam")

    # Loop through each exam column

    for i in range(grades.shape[1]):

        # Display the exam number

        print(f"\nExam {i + 1}")

        # Calculate and display the average

        print("Mean:", np.mean(grades[:, i]))

        # Calculate and display the median

        print("Median:", np.median(grades[:, i]))

        # Calculate and display the standard deviation

        print("Standard Deviation:", np.std(grades[:, i]))

        # Display the minimum grade

        print("Minimum:", np.min(grades[:, i]))

        # Display the maximum grade

        print("Maximum:", np.max(grades[:, i]))

    # Display overall statistics for all exams combined

    print("\nOverall Statistics")

    # Display the overall average

    print("Mean:", np.mean(grades))

    # Display the overall median

    print("Median:", np.median(grades))

    # Display the overall standard deviation

    print("Standard Deviation:", np.std(grades))

    # Display the overall minimum grade

    print("Minimum:", np.min(grades))

    # Display the overall maximum grade

    print("Maximum:", np.max(grades))

    # Display pass/fail results

    print("\nPass / Fail for Each Exam")

    # Loop through each exam column

    for i in range(grades.shape[1]):

        # Count students who scored 60 or higher

        passed = np.sum(grades[:, i] >= 60)

        # Count students who scored below 60

        failed = np.sum(grades[:, i] < 60)

        # Display the exam number

        print(f"\nExam {i + 1}")

        # Display the number of students who passed

        print("Passed:", passed)

        # Display the number of students who failed

        print("Failed:", failed)

    # Count the total number of grades

    total_grades = grades.size

    # Count the total number of passing grades

    passed_total = np.sum(grades >= 60)

    # Calculate the overall pass percentage

    pass_percentage = (passed_total / total_grades) * 100

    # Display the overall pass percentage

    print("\nOverall Pass Percentage: {:.2f}%".format(pass_percentage))

# Main program starts here

# Load the grades from the CSV file

grades = load_grades("grades.csv")

# Call the function to display all statistics

display_statistics(grades)

