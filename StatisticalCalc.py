from prettytable import PrettyTable
import numpy as np

size = int(input("Enter the size of the data: "))
xi = []
fi= []
fixi=[]
for i in range(size):
    value = float(input(f"Enter value {i + 1}: "))
    xi.append(value)
for i in range(size):
    value = float(input(f"Enter frequency {i + 1}: "))
    fi.append(value)

for i in range(size):
    fixi.append(xi[i] * fi[i])

mean = sum(fixi) / sum(fi)
mean = round(mean, 2)
print(f"Mean: {mean}")
variance = sum(fi[i] * (xi[i] - mean) ** 2 for i in range(size)) / sum(fi)
variance = round(variance, 2)
print(f"Variance: {variance}")
std_dev = np.sqrt(variance)
std_dev = round(std_dev, 2)
print(f"Standard Deviation: {std_dev}")
table = PrettyTable()
table.field_names = ["xi", "fi", "fixi"]
for i in range(size):
    table.add_row([xi[i], fi[i], fixi[i]])
print(table)

