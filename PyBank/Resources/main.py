import os
import csv

csvpath = os.path.join('Python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

Total_number_of_months = []
Total_net_amount_profit_losses = []
Average_amount_changes_profit_losses = []
Greatest_profit_increase_wdate = []
Greatest_profit_decrease_wdate = []

with open(csvpath) as budget:

	csvreader = csv.reader(budget, delimiter=',')
	
	header = next(csvreader)  

	for row in csvreader: 

    		Total_number_of_months.append(row[0])
    		Total_net_amount_profit_losses.append(int(row[1]))

	for i in bank_budget[bank_budget["Change"]==MaxIncrease]["Date"]:
    		i = MaxIncrease_Month

	for j in bank_budget[bank_budget["Change"]==MaxDecrease]["Date"]:
    		j = MaxDecrease_Month


print("Financial Analysis")
print("----------------------------")
print("Total Number of Months: " +str(Months))
print("Total: $" + str(Total))
print("Average Change: $" + str(round(AverageChange, int[2])))
print(f"Greatest Increase in Profits: ({total_months[greatest_increase_month])} (${(str(greatest_increase_value))})")
print(f"Greatest Decrease in Profits: ({total_months[greatest_decrease_month])} (${(str(greatest_decrease_value))})")
Result = open("Result.txt", "w")
Result.write("Financial Analysis")
Result.write("\n")
Result.write("----------------------------")
Result.write("\n")
Result.write("Total Number of Months: " +str(Months))
Result.write("\n")
Result.write("Total: $" + str(Total))
Result.write("\n")
Result.write("Average Change: $" + str(round(AverageChange, (int[2]))))
Result.write("\n")
Result.write(f"Greatest Increase in Profits: ({total_months[greatest_increase_month])} (${(str(greatest_increase_value))})")
Result.write("\n")
Result.write(f"Greatest Decrease in Profits: ({total_months[greatest_decrease_month])} (${(str(greatest_decrease_value))})")
Result.write("\n")

Result.close()
