<<<<<<< HEAD
# Define the functions for calculating the monthly installment for flat rate and reducing balance loans
def calculate_flat_rate_loan(amount, interest_rate, processing_fee, loan_term):
    # Calculate the total amount after adding the processing fee
    total_principal = amount + (amount * (processing_fee / 100))
    # Calculate the total interest based on the new principal
    total_interest = total_principal * (interest_rate / 100) * loan_term
    # Calculate the total amount to be repaid
    total_amount = total_principal + total_interest
    # Calculate the monthly installment
    monthly_installment = total_amount / (loan_term * 12)
    return monthly_installment

# Example usage
amount = 10000  # The borrowed amount
interest_rate = 5  # Annual interest rate in percentage
processing_fee = 2  # Processing fee in percentage
loan_term = 5  # Loan term in years

monthly_installment = calculate_flat_rate_loan(amount, interest_rate, processing_fee, loan_term)
print(f"The monthly installment for the loan is: {monthly_installment:.2f}")

def calculate_reducing_balance_loan(amount, interest_rate, processing_fee, loan_term):
    # Calculate the principal after adding the processing fee
    principal = amount + (amount * (processing_fee / 100))
        # Monthly interest rate
    monthly_interest_rate = (interest_rate / 100) / 12
    # Calculate the monthly installment using the formula for reducing balance loans
    monthly_installment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-loan_term * 12))
    return monthly_installment

# Get user input for the loan amount and term
loan_amount = float(input("Enter the loan amount: "))
loan_term_years = int(input("Enter the loan term in years: "))

# Constants for the interest rates and processing fee
flat_rate = 3.59  # Flat interest rate
reducing_balance_rate = 6.497  # Reducing balance interest rate
processing_fee = 2  # Loan processing fee

# Calculate monthly installments for both types of interest rates
flat_rate_monthly_installment = calculate_flat_rate_loan(loan_amount, flat_rate, processing_fee, loan_term_years)
reducing_balance_monthly_installment = calculate_reducing_balance_loan(loan_amount, reducing_balance_rate, processing_fee, loan_term_years)

# Print the results
print(f"Monthly installment for flat rate loan: {flat_rate_monthly_installment:.2f}")
print(f"Monthly installment for reducing balance loan: {reducing_balance_monthly_installment:.2f}")
=======
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
>>>>>>> 1bdf2a032eb8785ad6832e042a0bafaf939db505
