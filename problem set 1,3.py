outStandingBalance=float(raw_input("Enter the outstanding balance on your credit card:"))
annualInterestRate=float(raw_input("Enter the annual credit card interest rate as a decimal:"))
originalOutStandingBlance = outStandingBalance
monthlyInterestRate = annualInterestRate/12.0
minimumMonthlyPayment =10
monthsNeeded = 1
while(outStandingBalance > 0):
     outStandingBalance = outStandingBalance*(1+monthlyInterestRate)- minimumMonthlyPayment
     print monthsNeeded
     print outStandingBalance
     print minimumMonthlyPayment
     monthsNeeded = monthsNeeded + 1
     if(monthsNeeded > 12 and outStandingBalance >  0 ):
         outStandingBalance=originalOutStandingBlance
         minimumMonthlyPayment = minimumMonthlyPayment +10
         monthsNeeded=1
     
print "Monthly payment to pay off debt in 1 year:", minimumMonthlyPayment
print "Number of months needed: ", monthsNeeded
print "Balance: ", outStandingBalance
         
