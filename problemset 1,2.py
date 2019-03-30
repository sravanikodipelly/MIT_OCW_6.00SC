outStandingBlanace = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate= float(raw_input('Enter the annual credit card interest rate as a decimal: '))
minMonthlyPaymentRate= float(raw_input('Enter the minimum monthly pay rate as a decimal: '))
for i in range(1,13):
    print 'Month: ', i
    minMonthlyPayment = round(minMonthlyPaymentRate * outStandingBlanace, 2)
    print 'Minimum monthly payment: ', minMonthlyPayment
    interestPaid=round((annualInterestRate/12.0)*outStandingBlanace , 2)
    principalPaid = minMonthlyPayment - interestPaid
    print 'Principle paid: ', principalPaid
    outStandingBlanace= round(outStandingBlanace-principalPaid, 2)
    print 'Remaining balance: ', outStandingBlanace
