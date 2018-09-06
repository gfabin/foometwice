#CSCI-1511-B02-AUG-2018
#Greg Fabin ID #1227642 
#Car Salesman Program
#This program calcutes the total price of a car, including taxes and fees. 

#inputs set to floating point and not limited by decimal palces for accounting purposes
#after much ado and many hours I have added basic error handling so that a user cannot enter a letter or a negative number.    
    
while True:
    workPrice = input('Please enter the sale price of the vehicle: ')
    try:
        sellPrice = float(workPrice)
        if sellPrice > 0:
            break
        else:
            print("Please enter an amount greater than 0")
    except ValueError:
            print('Please enter a number')
            continue
tax = 0.075
totalTax = sellPrice * tax
licFee = 0.095
totalLicFee = sellPrice * licFee
prep = 49.50
destFee = 120.98

#Added orignial numbers including however many decimal places for accounting purposes
totalPrice = float(sellPrice + totalTax + totalLicFee + prep + destFee)

#Created rounded totals and converted to string for clean output
print('For a vehicle costing $' + str(sellPrice))
print('The sales tax rate is ' + str(float(tax * 100)) + '% making the total sales tax $' + str(round(totalTax, 2)))
print('There is a Licence Fee of ' + str(float(licFee * 100)) + '% making the total license fee for the vehicle $' + str(round(totalLicFee, 2)))
print('Dealer prep is $' + str(round(prep, 2)))
print('The destination fee is $' + str(round(destFee, 2)))
print('The total price for the vehicle is $' + str(round(totalPrice, 2)))