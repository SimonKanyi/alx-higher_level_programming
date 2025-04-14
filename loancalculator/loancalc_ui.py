import streamlit as st
import pandas as pd

def auto_logbook_loan(loan_amount, months):
    # ===== INPUTS =====
    additional_mv_premium = 0
    total_principle_loan = loan_amount + additional_mv_premium
    monthly_rate = 0.035  # 3.5% flat rate

    # ===== UPFRONT DEDUCTIONS =====
    admin_fee = 0.05 * total_principle_loan
    car_track_installation = 6000
    security_perfection = 3050
    disbursement_fee = 2500
    loan_insurance = 0.02 * loan_amount

    total_upfront_fees = admin_fee + car_track_installation + security_perfection + disbursement_fee + loan_insurance
    net_disbursement = total_principle_loan - total_upfront_fees

    # ===== MONTHLY PAYMENTS =====
    car_track_monthly = 2000
    principal_per_month = total_principle_loan / months
    interest_per_month = total_principle_loan * monthly_rate
    total_monthly_payment = principal_per_month + interest_per_month + car_track_monthly

    # ===== AMORTIZATION SCHEDULE =====
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

    # ===== SUMMARY =====
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
    # ===== INPUTS =====
    additional_mv_premium = 0
    total_principle_loan = loan_amount + additional_mv_premium
    monthly_rate = 0.06  # 6% flat rate

    # ===== UPFRONT DEDUCTIONS =====
    admin_fee = 0.05 * total_principle_loan
    car_track_installation = 9000
    disbursement_fee = 2500
    security_perfection = 2550
    loan_insurance = 0.02 * loan_amount

    total_upfront_fees = admin_fee + car_track_installation + disbursement_fee + security_perfection + loan_insurance
    net_disbursement = total_principle_loan - total_upfront_fees

    # ===== MONTHLY PAYMENTS =====
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

    # ===== SUMMARY =====
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
    st.title("Loan Calculator 🏦")
    st.markdown("Calculate loan repayments for **Auto Logbook** or **Bullet** loans.")

    # Inputs
    loan_type = st.radio("Loan Type:", ("Auto Logbook", "Bullet"))
    loan_amount = st.number_input("Loan Amount (KSH):", min_value=1000, step=1000, value=200000)
    months = st.slider("Loan Duration (Months):", 1, 36, 12)

    # Calculate button
    if st.button("Calculate"):
        with st.spinner("Generating schedule..."):
            if loan_type == "Auto Logbook":
                schedule, summary = auto_logbook_loan(loan_amount, months)
            else:
                schedule, summary = bullet_loan(loan_amount, months)

            # Display results
            st.subheader("Loan Summary 📊")
            st.table(summary)

            st.subheader("Repayment Schedule 📅")
            st.dataframe(schedule)

            # Download buttons
            csv_schedule = schedule.to_csv(index=False).encode('utf-8')
            csv_summary = summary.to_csv(index=False).encode('utf-8')

            col1, col2 = st.columns(2)
            with col1:
                st.download_button("Download Schedule", csv_schedule, "repayment_schedule.csv")
            with col2:
                st.download_button("Download Summary", csv_summary, "loan_summary.csv")

if __name__ == "__main__":
    main()