import csv
import os

# File paths
# Updated input file path
input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "budget_data_output.txt")

# Initialize variables
month_count = 0
total_sum = 0
month_of_record = []
month_over_month_changes = []
highest_increase = ["", 0]
highest_decrease = ["", float("inf")]

# Read input data and process
with open(input_file) as input_data:
    reader = csv.reader(input_data)
    header = next(reader)

    # Process the first row
    first_row = next(reader)
    month_count += 1
    total_sum += int(first_row[1])
    prev_value = int(first_row[1])

    for row in reader:
        # Accumulate values and calculate changes
        month_count += 1
        total_sum += int(row[1])
        current_value = int(row[1])
        change = current_value - prev_value

        # Record changes and months
        month_over_month_changes.append(change)
        month_of_record.append(row[0])

        # Find highest increase and decrease
        if change > highest_increase[1]:
            highest_increase = [row[0], change]

        if change < highest_decrease[1]:
            highest_decrease = [row[0], change]

        # Update previous value for the next iteration
        prev_value = current_value

# Calculate average change
average_change = sum(month_over_month_changes) / len(month_over_month_changes)

# Generate output
generated_output = (
    f"Budget Analysis Output\n"
    f"----------------------------\n"
    f"Total Count of Months: {month_count}\n"
    f"Total Sum of Changes: ${total_sum}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Highest Increase: {highest_increase[0]} (${highest_increase[1]})\n"
    f"Highest Decrease: {highest_decrease[0]} (${highest_decrease[1]})\n"
)

# Print to terminal
print(generated_output)

# Write to file
with open(output_file, "w") as txt_file:
    txt_file.write(generated_output)
