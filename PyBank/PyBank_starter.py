# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")# Input file path
file_to_output = os.path.join(os.path.dirname(__file__), "analysis", "budget_analysis.txt")# Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
months = []
print("Looking for file at:", os.path.abspath(file_to_load))
# Open and read the CSV
try:
    with open(file_to_load, "r") as financial_data:
        reader = csv.reader(financial_data)

        # Skip the header row
        header = next(reader)

        # Extract the first row to initialize variables
        first_row = next(reader)
        total_months += 1
        total_net += int(first_row[1])
        previous_net = int(first_row[1])

        # Process each subsequent row of data
        for row in reader:
            # Track the total months
            total_months += 1

            # Track the total net amount
            total_net += int(row[1])

            # Calculate the monthly change in profits/losses
            net_change = int(row[1]) - previous_net
            net_change_list.append(net_change)
            months.append(row[0])

            # Update the previous net amount
            previous_net = int(row[1])

    # Calculate the average net change across months
    average_change = sum(net_change_list) / len(net_change_list)

    # Determine the greatest increase and decrease in profits
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)
    greatest_increase_month = months[net_change_list.index(greatest_increase)]
    greatest_decrease_month = months[net_change_list.index(greatest_decrease)]

    # Generate the output summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )

    # Print the output
    print(output)

    # Write the results to a text file
    os.makedirs(os.path.dirname(file_to_output), exist_ok=True)
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)

except FileNotFoundError:
    print(f"Error: The file '{file_to_load}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
