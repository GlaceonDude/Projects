#Anthony Barrante
#ITP 100
#This program inputs a paragraph of text
#Caesar ciphers it into file "encrypt.txt"
#and copies it to file "copyfile.py"

#Take in values and display purpose
print("This program encrypts a message\n")
message = str(input("Please enter your message: "))
shift = int(input("Please enter the distance value for the Caesar Cipher: "))
code = ""

encryptFile=open("encrypt.txt", 'w') #Open or create encrypt.txt file
#Caesar Cipher
for ch in message:
    ordValue = ord(ch)
    cipherValue = (ordValue + shift)
    if cipherValue > 127:
        cipherValue = shift - (127 - ordValue + 1)
    code += chr(cipherValue)
print(code, " was placed into encrypt.txt")
encryptFile.write(code)

encryptFile.close()
while True:
    encryptFile = open("encrypt.txt", 'r')
    copyFile = open("copyfile.py", 'w')
    while True:
        line = encryptFile.readline()
        copyFile.write(str(line))
        if line == "":
            break
        print(line, " was moved into copyfile.py")
    copyFile.close()
    encryptFile.close()
    break
    
