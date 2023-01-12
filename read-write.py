# Reading and Writing Files

months = open("months.txt")

for month in months:
    print(month.strip())

months.close()