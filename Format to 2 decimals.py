#New program
# Request the input
NumKilometers = float(input("Enter number of kilometers travelled:"))

# Compute the result
NautMiles = float(NumKilometers*54/100)
NautMiles = round(NautMiles,9)


# Display the result
print("The number nautical miles travelled equals", NautMiles)


