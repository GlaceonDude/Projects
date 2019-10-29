#Prompt user to enter a message
code = str(input("Please enter the coded text: "))
# Prompt user to enter a shift
shift = int(input("Please enter the distance value: "))
# Print the decrypted message
plainText = ""

#Decrypt Loop
for ch in code:
    #Set the number of the character
    ordValue = ord(ch)
    #Subtract the distance value from the coded letter
    cipherValue = (ordValue - shift)
    if cipherValue > 0:
        plainText += chr(cipherValue)

    if cipherValue < 0:
        cipherValue = 127 - (shift - (1 + ordValue))
        plainText += chr(cipherValue)
print(plainText)
