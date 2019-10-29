def myRange(start, stop = None, step = None):
    """Acts like Pythons range function but does not use the range function."""
    i = 0
    my_list = []
    while stop == None:
        my_list.append(i) #add integer to list
        i = i+1           #increment counter
        if i == start:
            break
    while stop != None and step == None:
        my_list.append(start)       #Add integer of start to list instead here
        start = start + 1           #Increment start as counter
        if start == stop:           #Stop when reaching the end of range
            break
    while stop != None and step != None and start > stop: #For iterations of
        my_list.append(start)                       #off step ranges
        start = start + step
        if start <= stop:
            break
    while stop != None and step != None and start < stop: #2nd off step ranges
        my_list.append(start)
        start = start + step
        if start >= stop:
            break

    return(i)
def main():
    print(myRange(10))
    print(myRange(1, 10))
    print(myRange(1, 10, 2))
    print(myRange(10, 1, -1))

main()

