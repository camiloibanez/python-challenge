import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")

def average(numbers):

    average = sum(numbers)/len(numbers)
    return average

with open(file_path, 'r') as csvfile:
    budget_data_reader = csv.reader(csvfile, delimiter=',')

    budget_data_header = next(budget_data_reader)

    total_months = 0
    net_total_profit_loss = 0
    profit_loss = []
    months = []
    
    for row in budget_data_reader:
        total_months += 1
        net_total_profit_loss += int(row[1])
        profit_loss.append(int(row[1]))
        months.append(row[0])

    average_change = average(profit_loss)

    max_profit = max(profit_loss)
    min_loss = min(profit_loss)

    max_profit_month = months[profit_loss.index(max_profit)]
    min_loss_month = months[profit_loss.index(min_loss)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_loss}")
print("Average Change: $%.2f" % average_change)
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_loss_month} (${min_loss})")

output_path = os.path.join("financial_analysis.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_profit_loss}\n")
    txtfile.write(f"Average Change: $%.2f" % average_change + "\n")
    txtfile.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_loss_month} (${min_loss})")

    txtfile.close()