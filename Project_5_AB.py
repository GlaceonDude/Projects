#Anthony Barrante
#ITP 100
#Chapter 5 Project
#This program uses functions to convert numbers
#from different bases


baseDictionary = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10,'B':11, 'C':12,'D':13,'E':14,'F':15}


def repToDecimal(fromNumber, fromBase):                                      
    toNumber = 0                                                             
    exponent = 0                                                                
    for i in range ((len(fromNumber)),0, -1):    #for: length of forNumber starting from right to left counting to zero
        toNumber += baseDictionary[fromNumber[i-1]] * (int(fromBase) ** exponent)     #add the current toNumber to the new calculated position
        exponent += 1       #increment exponent as i traverses position
    print(toNumber) 

def main():
    
    fromNumber = input("Please enter the number to be converted to base 10: ")
    fromBase = int(input("Please enter the base to convert from: "))

    fromNumber = fromNumber.upper() #This function brings all letters to uppercase

    print("Here is the conversion using numbers of your choosing: ")
    repToDecimal(fromNumber, fromBase) #convert number from numbers of choice

    print("Here's some conversions from other bases: ")
    print("From base 2: ")
    (repToDecimal('10', 2)) #print from base 2
    print("From base 8: ")
    (repToDecimal('10', 8))  #print from base 8
    print("From base 10: ")
    (repToDecimal('10', 10))  #print from base 10
    print("From base 16: ")
    (repToDecimal('10', 16)) #print from base 16

main()
