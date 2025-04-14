import pandas as pd

def get_user_input():
    while True:
        try:
            loan_type = input("Choose loan type (1-Auto Logbook / 2-Bullet): ").strip()
            if loan_type not in ["1", "2"]:
                raise ValueError("Invalid choice. Enter 1 or 2.")
            
            loan_amount = float(input("Enter loan amount (KSH): "))
            months = int(input("Enter loan duration (months): "))
            
            if loan_amount <= 0 or months <= 0:
                raise ValueError("Loan amount/duration must be positive.")
            
            return loan_type, loan_amount, months
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

def auto_logbook_loan(loan_amount, months):
    additional_mv_premium = 0
    total_principle_loan = loan_amount + additional_mv_premium
    monthly_rate = 0.035  # 3.5% flat rate

    # Upfront deductions
    admin_fee = 0.05 * total_principle_loan
    car_track_installation = 6000
    security_perfection = 3050
    disbursement_fee = 2500
    loan_insurance = 0.02 * loan_amount

    total_upfront_fees = admin_fee + car_track_installation + security_perfection + disbursement_fee + loan_insurance
    net_disbursement = total_principle_loan - total_upfront_fees

    # Monthly payments
    car_track_monthly = 2000
    principal_per_month = total_principle_loan / months
    interest_per_month = total_principle_loan * monthly_rate
    total_monthly_payment = principal_per_month + interest_per_month + car_track_monthly

    # Amortization schedule
    schedule = []
    balance = total_principle_loan

    for month in range(1, months + 1):
        interest = total_principle_loan * monthly_rate
        principal = principal_per_month
        balance -= principal
        schedule.append({
            "Month": month,
            "Principal": round(principal, 2),
            "Interest": round(interest, 2),
            "CarTrack Fee": car_track_monthly,
            "Total Payment": round(total_monthly_payment, 2),
            "Balance": round(balance, 2)
        })

    # Summary
    total_repayable = total_monthly_payment * months
    summary = {
        "Loan Type": "Auto Logbook",
        "Loan Amount (KSH)": loan_amount,
        "Duration (Months)": months,
        "Net Disbursement (KSH)": round(net_disbursement, 2),
        "Monthly Payment (KSH)": round(total_monthly_payment, 2),
        "Total Repayable (KSH)": round(total_repayable, 2)
    }

    return pd.DataFrame(schedule), pd.DataFrame([summary])

def bullet_loan(loan_amount, months):
    additional_mv_premium = 0
    total_principle_loan = loan_amount + additional_mv_premium
    monthly_rate = 0.06  # 6% flat rate

    # Upfront deductions
    admin_fee = 0.05 * total_principle_loan
    car_track_installation = 9000
    disbursement_fee = 2500
    security_perfection = 2550
    loan_insurance = 0.02 * loan_amount

    total_upfront_fees = admin_fee + car_track_installation + disbursement_fee + security_perfection + loan_insurance
    net_disbursement = total_principle_loan - total_upfront_fees

    # Monthly payments (bullet structure)
    interest_per_month = total_principle_loan * monthly_rate
    car_track_monthly = 0
    payments = []

    for month in range(1, months + 1):
        if month < months:
            principal = 0
            total_payment = interest_per_month + car_track_monthly
        else:
            principal = total_principle_loan
            total_payment = principal + interest_per_month + car_track_monthly

        payments.append({
            "Month": month,
            "Principal": round(principal, 2),
            "Interest": round(interest_per_month, 2),
            "CarTrack Fee": car_track_monthly,
            "Total Payment": round(total_payment, 2)
        })

    # Summary
    total_repayable = sum(p["Total Payment"] for p in payments)
    summary = {
        "Loan Type": "Bullet",
        "Loan Amount (KSH)": loan_amount,
        "Duration (Months)": months,
        "Net Disbursement (KSH)": round(net_disbursement, 2),
        "Total Repayable (KSH)": round(total_repayable, 2)
    }

    return pd.DataFrame(payments), pd.DataFrame([summary])

def main():
    loan_type, loan_amount, months = get_user_input()
    
    if loan_type == "1":
        schedule, summary = auto_logbook_loan(loan_amount, months)
    else:
        schedule, summary = bullet_loan(loan_amount, months)
    
    print("\n=== LOAN SUMMARY ===")
    print(summary.to_string(index=False))
    print("\n=== REPAYMENT SCHEDULE ===")
    print(schedule.to_string(index=False))

if __name__ == "__main__":
    main()