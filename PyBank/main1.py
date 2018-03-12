budget_data = "budget_data_1.csv"

import csv

months = []
revenue = []

with open(budget_data, newline='') as csvfile:
    budget_lists = csv.reader(csvfile, delimiter=',')
    for row in budget_lists:
        months.append(row[0])
        revenue.append(row[1])

#remove the words "Data" and "Revenue" from the lists 
months.remove("Date")
revenue.remove("Revenue")

#converting revenue values to integers
for i in range(len(revenue)):
    revenue[i]=int(revenue[i])

#counting the number of months in a months list
total_months = len(months)

#sum revenue, average revenue
total_revenue = sum(revenue)
average_revenue = int(total_revenue/len(revenue))

#Greatest Increase in Revenue
max_revenue = max(revenue)
index_max = revenue.index(max_revenue)
month_max = months[index_max]

#Greatest Decrease in Revenue
min_revenue = min(revenue)
index_min = revenue.index(min_revenue)
month_min = months[index_min]

#printing it all out
print("Total Months: " + str(total_months))
print("Total Revenue: " + str(total_revenue))
print("average Revenue Change: $" + str(average_revenue))
print("Greatest Increase in Revenue: " + str(month_max) + " ($" + str(max_revenue) + ")")
print("Greatest Decrease in Revenue: " + str(month_min) + " ($" + str(min_revenue) + ")")

#creating and writting to a text file
result = open("resultmain1.txt", "w") 
 
result.write("Total Months: " + str(total_months) + "\n") 
result.write("Total Revenue: " + str(total_revenue) + "\n") 
result.write("average Revenue Change: $" + str(average_revenue)+ "\n") 
result.write("Greatest Increase in Revenue: " + str(month_max) + " ($" + str(max_revenue) + ")" + "\n")
result.write("Greatest Decrease in Revenue: " + str(month_min) + " ($" + str(min_revenue) + ")" + "\n") 
 
result.close() 
