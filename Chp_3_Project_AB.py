#Anthony Barrante
#ITP 100
#Chapter 3 Project
#This program totals the numbers that the user inputs until
#the user presses Enter to exit the program


Sum = float(0.0) 

while True:
    UserData = str(input("Please enter a number or press Enter when finished: "))
    if UserData == "": #If Enter is pressed without input, program will go to print
        break
    else:
        StorageNum = float(UserData) #Temporarily stores user input for sum calculation
        Sum += StorageNum
#End of loop
print("The sum of the numbers entered is: ", Sum)
