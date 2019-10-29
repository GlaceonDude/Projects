#Ask for inputs
StartSalary = float(input("Please enter the starting salary: "))
PercentRaise = float(input("Please enter the percentage increase: "))
YearsInSchedule = int(input("Please enter the number of years on the schedule: "))

# Compute and display the results

for years in range(YearsInSchedule):
    iteration = int(years)
    print(iteration+1, "%.2f"% StartSalary) #Prints initial
    NewSalary = (StartSalary +(StartSalary*(PercentRaise/100)))
    StartSalary = float(NewSalary)    #Ready the StartSalary for next year
    
