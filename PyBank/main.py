import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")

def average(numbers):

    average = sum(numbers)/len(numbers)
    return average

def to_currency(value):
    return '${:,}'.format(value)

with open(file_path, 'r') as csvfile:
    budget_data_reader = csv.reader(csvfile, delimiter=',')

    budget_data_header = next(budget_data_reader)

    total_months = 0
    net_total_profit_loss = 0
    change_in_profit_loss = []
    months = []

    previous_profit_loss = 0

    for row in budget_data_reader:
        # Adding another month to the list of total months counted
        total_months += 1
        # Adding to the total net profit loss
        net_total_profit_loss += int(row[1])
        # Appending the date of the record
        months.append(row[0])
        # Calculating the change in profit loss from the previous month to the next month
        next_profit_loss = int(row[1])

        change_in_profit_loss.append(next_profit_loss - previous_profit_loss)

        previous_profit_loss = int(row[1])
    # Removing the first profit/loss because we don't have a previous month
    change_in_profit_loss.pop(0)
    average_change = average(change_in_profit_loss)

    max_profit_change = max(change_in_profit_loss)
    min_loss_change = min(change_in_profit_loss)

    max_profit_change_index = change_in_profit_loss.index(max_profit_change) + 1
    min_loss_change_index = change_in_profit_loss.index(min_loss_change) + 1

    max_profit_month = months[max_profit_change_index]
    min_loss_month = months[min_loss_change_index]

    net_total_profit_loss_currency = to_currency(net_total_profit_loss)

    

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total_profit_loss_currency}")
print("Average Change: $%.2f" % average_change)
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_change})")
print(f"Greatest Decrease in Profits: {min_loss_month} (${min_loss_change})")

output_path = os.path.join("financial_analysis.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: {net_total_profit_loss_currency}\n")
    txtfile.write(f"Average Change: $%.2f" % average_change + "\n")
    txtfile.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit_change})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_loss_month} (${min_loss_change})")

    txtfile.close()