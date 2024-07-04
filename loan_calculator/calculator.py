def calculate_loan_schedule(loan_amount, loan_duration, annual_interest_rate=0.06404, application_fee_rate=0.02):
    # Calculate the principal amount
    principal = loan_amount + (loan_amount * application_fee_rate)
    
    # Calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    
    # Calculate the monthly installment using the formula for an annuity
    monthly_payment = (monthly_interest_rate * principal) / (1 - (1 + monthly_interest_rate) ** -loan_duration)
    
    # Initialize the loan schedule list
    loan_schedule = []
    
    # Calculate the loan schedule
    for month in range(1, loan_duration + 1):
        # Calculate interest for the current month
        interest_payment = principal * monthly_interest_rate
        
        # The principal payment is the monthly payment minus the interest payment
        principal_payment = monthly_payment - interest_payment
        
        # Append the details to the loan schedule
        loan_schedule.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Monthly Installment": monthly_payment,
            "Remaining Balance": principal - principal_payment
        })
        
        # Reduce the principal by the amount paid towards the principal
        principal -= principal_payment
    
    return loan_schedule

# Prompt the user for the desired loan amount and loan duration
loan_amount = float(input("Enter the desired loan amount: "))
loan_duration = int(input("Enter the desired loan duration (in months): "))

# Calculate the loan schedule
loan_schedule = calculate_loan_schedule(loan_amount, loan_duration)

# Print the loan schedule
print("Loan Schedule:")
print(f"{'Month':<10}{'Principal Payment':<20}{'Interest Payment':<20}{'Monthly Installment':<20}{'Remaining Balance':<20}")
for payment in loan_schedule:
    print(f"{payment['Month']:<10}{payment['Principal Payment']:<20.2f}{payment['Interest Payment']:<20.2f}{payment['Monthly Installment']:<20.2f}{payment['Remaining Balance']:<20.2f}")
