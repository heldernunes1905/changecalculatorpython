def calculatechange(change):
    
    changeamounts = [0] * 13 #create array with 13 spots for all the different types of changes that will be given out

    while(change > 0): #keeps going until all the change has been counted
        change = round(change,2) # kept rounding like 0.45 to .449999999999999999
        if(change >= 100):
            changeamounts[0] += 1
            change -= 100
        elif(change >= 50):
            changeamounts[1] += 1
            change -= 50
        elif(change >= 20):
            changeamounts[2] += 1
            change -= 20
        elif(change >= 10):
            changeamounts[3] += 1
            change -= 10
        elif(change >= 5):
            changeamounts[4] += 1
            change -= 5
        elif(change >= 2):
            changeamounts[5] += 1
            change -= 2
        elif(change >= 1):
            changeamounts[6] += 1
            change -= 1
        elif(change >= 0.5):
            changeamounts[7] += 1
            change -= 0.5
        elif(change >= 0.2):
            changeamounts[8] += 1
            change -= 0.2
        elif(change >= 0.1):
            changeamounts[9] += 1
            change -= 0.1
        elif(change >= 0.05):
            changeamounts[10] += 1
            change -= 0.05
        elif(change >= 0.02):
            changeamounts[11] += 1
            change -= 0.02
        elif(change >= 0.01):
            changeamounts[12] += 1
            change -= 0.01

    return changeamounts

#paying = 54.45 #Test Value for what amount due
#payed = 100 #Test Value for what user inserted

#value that has to be payed
print("Value that needs to be payed: ")
paying = input()
paying = round(float(paying),2) #convert to float with 2 decimal places

#value that user inserted
print("Value inserted by user: ")
payed = input() 
payed = round(float(payed),2) #convert to float with 2 decimal places

change = payed - paying #change needed to return


valuechanged = calculatechange(change) #send values to function where it can be calculated


cointype = ["Hundred", "Fifty", "Twenty", "Ten", "Five", "Two", "One", "Fifty Cents", "Twenty Cents", "Ten Cents", "Five Cents", "Two Cents", "One Cents"] #numbers of currency

counter = 0 #simple counter

for c in valuechanged:
    if(c != 0):
        print("%s: %d" % (cointype[counter],c))
    counter +=1

