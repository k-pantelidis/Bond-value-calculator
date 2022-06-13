import matplotlib.pyplot as plt

totalVal = 0
totalCountArr = []
totalValArr = []
graphs = []
faceAmount = float(input("Insert Face Value Amount (default $24,000): ") or 24000.0)
interestRate = float(input("Insert Interest Rate in % (default 10%): " ) or 10) / 100
paymentPeriods = float(input("Insert Payment Periods per Year (default 4 periods): ") or 4)
maturity = float(input("Insert maturity (default 4 years): ") or 4)
discountRate = float(input("Insert Discount Rate in % (default 10%):") or 10) / 100

def calculateYears(periodCount:int = 1, faceAmount:float = 24000.0, interestRate:float = 0.1, paymentPeriods:float= 4.0, maturity:float= 4.0, discountRate:float= 0.1):
    periods = paymentPeriods * maturity
    beginningBalance = faceAmount
    interestPayment = (beginningBalance * interestRate)/paymentPeriods
    principalPayment = 0
    endingBalance = 0
    tenor = 0
    discountFactor = 0
    presentValue = 0

    if(periodCount == (paymentPeriods*maturity)) :
        principalPayment = beginningBalance
    else:
        principalPayment = 0

    endingBalance = beginningBalance - principalPayment
    tenor = periodCount / paymentPeriods
    discountFactor = 1/((1+discountRate)**tenor)
    presentValue = discountFactor*(interestPayment + principalPayment)
    if(periodCount == 1):
        print("Period\tBeginning Bal.\tInterest Pmt.\tPrincipal Pmt.\tEnding Bal.\tTenor\tDiscount Factor\tPresent Value of Payment")
    print(periodCount, "\t\t", round(beginningBalance), "\t\t\t", round(interestPayment), "\t\t\t", round(principalPayment), "\t\t\t\t", round(endingBalance), "\t\t", tenor, "\t", round(discountFactor, 4), "\t\t\t", round(presentValue))
    totalValArr.append(presentValue)
    if(periodCount < periods):
        presentValue += calculateYears(periodCount + 1, faceAmount, interestRate, paymentPeriods, maturity, discountRate)
    return presentValue

totalVal = calculateYears(1, faceAmount, interestRate, paymentPeriods, maturity, discountRate)
print("PV of Cash Flows", round(totalVal))
print("Price", round(((totalVal/faceAmount) * 100), 2))

#BONUS
totalValArr = []
totalVal = calculateYears(1, faceAmount, interestRate, paymentPeriods, 2, discountRate)
graphs.append(totalValArr)
#cleaning
totalValArr = []
totalVal = calculateYears(1, faceAmount, interestRate, paymentPeriods, 3, discountRate)
graphs.append(totalValArr)
#cleaning
totalValArr = []
totalVal = calculateYears(1, faceAmount, interestRate, paymentPeriods, 4, discountRate)
graphs.append(totalValArr)

plt.plot(list(range(1, len(graphs[0]) + 1)), graphs[0], 'r', label='2 year maturity')
plt.plot(list(range(1, len(graphs[1]) + 1)), graphs[1], 'g', label='3 year maturity')
plt.plot(list(range(1, len(graphs[2]) + 1)), graphs[2], 'b', label='4 year maturity')

plt.ylabel('Value in USD')
plt.xlabel('Periods')
plt.legend()
plt.show()



