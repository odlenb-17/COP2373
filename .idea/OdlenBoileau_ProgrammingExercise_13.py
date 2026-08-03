import sqlite3

import random

import matplotlib.pyplot as plt

# ---------------------------------------------------------

# Function 1

# Create the database and insert the 2023 population data

# ---------------------------------------------------------

def create_database():

    # Connect to the database

    conn = sqlite3.connect("population_OB.db")

    cursor = conn.cursor()

    # Delete the table if it already exists

    cursor.execute("DROP TABLE IF EXISTS population")

    # Create the population table

    cursor.execute("""

    CREATE TABLE population(

        city TEXT,

        year INTEGER,

        population INTEGER

    )

    """)

    # List of Florida cities with 2023 population

    cities = {

        "Miami": 455924,

        "Orlando": 320742,

        "Tampa": 403364,

        "Jacksonville": 985843,

        "Naples": 19618,

        "Fort Myers": 98432,

        "Cape Coral": 224455,

        "Sarasota": 57513,

        "Tallahassee": 202221,

        "Pensacola": 54812

    }

    # Insert the 2023 data

    for city, population in cities.items():

        cursor.execute(

            "INSERT INTO population VALUES (?, ?, ?)",

            (city, 2023, population)

        )

    conn.commit()

    conn.close()

# ---------------------------------------------------------

# Function 2

# Simulate population changes for the next 20 years

# ---------------------------------------------------------

def simulate_population():

    conn = sqlite3.connect("population_OB.db")

    cursor = conn.cursor()

    # Get the original city data

    cursor.execute("SELECT city, population FROM population WHERE year=2023")

    rows = cursor.fetchall()

    # Generate data from 2024 through 2043

    for city, population in rows:

        current_population = population

        for year in range(2024, 2044):

            # Random growth or decline between -2% and +5%

            rate = random.uniform(-0.02, 0.05)

            current_population = int(current_population * (1 + rate))

            cursor.execute(

                "INSERT INTO population VALUES (?, ?, ?)",

                (city, year, current_population)

            )

    conn.commit()

    conn.close()

# ---------------------------------------------------------

# Function 3

# Display a graph for the selected city

# ---------------------------------------------------------

def display_population():

    conn = sqlite3.connect("population_OB.db")

    cursor = conn.cursor()

    cities = [

        "Miami",

        "Orlando",

        "Tampa",

        "Jacksonville",

        "Naples",

        "Fort Myers",

        "Cape Coral",

        "Sarasota",

        "Tallahassee",

        "Pensacola"

    ]

    # Show the city options

    print("\nChoose one of the following cities:\n")

    for index, city in enumerate(cities, start=1):

        print(index, "-", city)

    choice = int(input("\nEnter a number (1-10): "))

    selected_city = cities[choice - 1]

    # Retrieve the data

    cursor.execute(

        "SELECT year, population FROM population WHERE city=? ORDER BY year",

        (selected_city,)

    )

    data = cursor.fetchall()

    years = []

    populations = []

    for year, population in data:

        years.append(year)

        populations.append(population)

    # Create the graph

    plt.plot(years, populations, marker="o")

    plt.title(selected_city + " Population Growth")

    plt.xlabel("Year")

    plt.ylabel("Population")

    plt.grid(True)

    plt.show()

    conn.close()

# ---------------------------------------------------------

# Main Program

# ---------------------------------------------------------

create_database()

simulate_population()

display_population()

print("\nProgram Finished!")