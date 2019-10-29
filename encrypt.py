# Prompt user to enter a message
clearText = input("Please enter a message: ")
# Prompt user to enter a shift
shift = int(input("Please enter distance value: "))
# Print the encrypted message
code = ""
for ch in clearText:
    ordValue = ord(ch)
    cipherValue = (ordValue + shift)
    if cipherValue > 127:
        cipherValue = shift - (127 - ordValue + 1)
    code += chr(cipherValue)
print(code)
