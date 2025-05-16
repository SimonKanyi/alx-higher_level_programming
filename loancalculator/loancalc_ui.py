import streamlit as st
import pandas as pd
import plotly.express as px

# ========================================================================
# Calculation Function with Monthly Tracker Fee
# ========================================================================

def calculate_loan(loan_amount, months, monthly_rate, 
                 admin_fee_pct=5, security_fee=3050, 
                 disbursement_fee=2500, insurance_pct=2,
                 tracker_install=6000, tracker_monthly=2000):  # Added monthly tracker

    # Upfront deductions
    admin_fee = loan_amount * (admin_fee_pct/100)
    insurance = loan_amount * (insurance_pct/100)
    total_deductions = admin_fee + security_fee + disbursement_fee + insurance + tracker_install
    net_disbursement = loan_amount - total_deductions

    # Monthly calculations
    principal_per_month = loan_amount / months
    fixed_interest = loan_amount * monthly_rate
    monthly_tracker = tracker_monthly  # New monthly fee
    
    total_monthly_payment = principal_per_month + fixed_interest + monthly_tracker

    schedule = []
    balance = loan_amount
    
    for month in range(1, months + 1):
        payment = total_monthly_payment
        balance -= principal_per_month
        
        schedule.append({
            "Month": month,
            "Principal (KSH)": round(principal_per_month, 2),
            "Interest (KSH)": round(fixed_interest, 2),
            "Tracker Fee (KSH)": tracker_monthly,
            "Total Payment (KSH)": round(payment, 2),
            "Balance (KSH)": round(balance, 2)
        })

    # Enhanced summary
    summary = {
        "Loan Amount": loan_amount,
        "Total Deductions": total_deductions,
        "Net Disbursement": net_disbursement,
        "Monthly Tracker": tracker_monthly,
        "Total Tracker Fees": tracker_monthly * months,
        "Total Repayable": total_monthly_payment * months
    }

    return pd.DataFrame(schedule), pd.DataFrame([summary])

# ========================================================================
# Streamlined UI with Adjustable Fees
# ========================================================================

def main():
    st.set_page_config(page_title="Loan Calculator Ultra", layout="wide")
    st.title("🏦 Advanced Loan Calculator")
    
    # Main inputs
    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input("Loan Amount (KSH):", 
                                    min_value=1000, 
                                    value=300000,
                                    step=1000)
        months = st.slider("Loan Term (months):", 1, 60, 24)
        
    with col2:
        monthly_rate = st.number_input("Monthly Interest Rate (%):",
                                     min_value=0.1,
                                     max_value=50.0,
                                     value=3.5,
                                     step=0.5) / 100
        
        with st.expander("Fee Configuration ⚙️"):
            cols = st.columns(2)
            with cols[0]:
                admin_fee_pct = st.number_input("Admin Fee (%):", 0.0, 20.0, 5.0)
                security_fee = st.number_input("Security Fee:", 0, 10000, 3050)
                tracker_install = st.number_input("Tracker Installation:", 0, 20000, 6000)
            with cols[1]:
                disbursement_fee = st.number_input("Disbursement Fee:", 0, 10000, 2500)
                insurance_pct = st.number_input("Insurance (%):", 0.0, 20.0, 2.0)
                tracker_monthly = st.number_input("Monthly Tracker Fee:", 0, 5000, 2000)

    if st.button("Generate Full Report"):
        schedule_df, summary_df = calculate_loan(
            loan_amount, months, monthly_rate,
            admin_fee_pct, security_fee, 
            disbursement_fee, insurance_pct,
            tracker_install, tracker_monthly
        )
        
        # Compact Financial Summary
        st.subheader("📊 Financial Summary")
        summ = summary_df.iloc[0]
        
        cols = st.columns(4)
        metrics = [
            ("Loan Amount", f"KSH {summ['Loan Amount']:,.2f}"),
            ("Total Deductions", f"KSH {summ['Total Deductions']:,.2f}"),
            ("Net Disbursement", f"KSH {summ['Net Disbursement']:,.2f}"),
            ("Monthly Tracker", f"KSH {summ['Monthly Tracker']:,.2f}"),
            ("Total Tracker Fees", f"KSH {summ['Total Tracker Fees']:,.2f}"),
            ("Total Repayable", f"KSH {summ['Total Repayable']:,.2f}")
        ]
        
        # Reduced font size using HTML
        for idx, (label, value) in enumerate(metrics):
            with cols[idx%4]:
                st.markdown(f"""
                <div style='border-left: 3px solid #4a86e8; padding-left: 1rem; margin: 0.5rem 0;'>
                    <p style='margin:0; font-size:14px; color:#666;'>{label}</p>
                    <p style='margin:0; font-size:16px; font-weight:bold;'>{value}</p>
                </div>
                """, unsafe_allow_html=True)

        # Detailed Schedule
        st.subheader("📅 Payment Schedule")
        st.dataframe(
            schedule_df.style.format({
                'Principal (KSH)': '{:,.2f}',
                'Interest (KSH)': '{:,.2f}',
                'Tracker Fee (KSH)': '{:,.2f}',
                'Total Payment (KSH)': '{:,.2f}',
                'Balance (KSH)': '{:,.2f}'
            }),
            height=400
        )

if __name__ == "__main__":
    main()