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
