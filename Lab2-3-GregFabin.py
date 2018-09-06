#CSCI-1511-B02-AUG-2018
#Greg Fabin ID #1227642
#Tipper Program

#This caculates a 15 or 20 percent tip for customers with a given bill

while True:
    tempBill = input('Please enter the cost of the meal: ')
    try:
        bill = float(tempBill)
        if bill > 0:
            break
        else:
            print("Please enter an amount greater than 0")
    except ValueError:
            print('Please enter a number')
            continue
    
tipFifteen = (bill * 0.15)
tipTwenty = (bill * 0.20)

#added fancy concatenation for the exerpiece
print('A 15% tip for a bill of $' + str(bill) + ' is $' + str(round(tipFifteen, 2)) + ' and the total bill will be $' + str(round((tipFifteen + bill), 2)))
print('A 20% tip for a bill of $' + str(bill) + ' is $' + str(round(tipTwenty, 2)) + ' and the total bill will be $' + str(round((tipTwenty + bill), 2)))

