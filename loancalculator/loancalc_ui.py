import streamlit as st
import pandas as pd
import plotly.express as px
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# ========================================================================
# Loan Calculation Function with Fixed Rate
# ========================================================================

def calculate_loan(loan_amount, months, monthly_rate, one_time_fee=0, monthly_fee=0):
    total_principle = loan_amount + one_time_fee
    principal_per_month = total_principle / months
    fixed_interest = loan_amount * monthly_rate  # Fixed monthly interest
    
    schedule = []
    balance = total_principle
    
    for month in range(1, months + 1):
        payment = principal_per_month + fixed_interest + monthly_fee
        balance -= principal_per_month
        
        schedule.append({
            "Month": month,
            "Principal (KSH)": round(principal_per_month, 2),
            "Interest (KSH)": round(fixed_interest, 2),
            "Fees (KSH)": round(monthly_fee, 2),
            "Total Payment (KSH)": round(payment, 2),
            "Balance (KSH)": round(balance, 2)
        })
    
    total_repayable = payment * months
    summary = {
        "Loan Amount": loan_amount,
        "Monthly Rate": f"{monthly_rate*100}%",
        "Total Interest": fixed_interest * months,
        "Total Repayable": total_repayable
    }
    
    return pd.DataFrame(schedule), pd.DataFrame([summary])

# ========================================================================
# Interactive UI
# ========================================================================

def main():
    st.set_page_config(page_title="Loan Calculator", layout="centered")
    st.title("🏦 Interactive Loan Calculator")
    
    # User Inputs
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
        monthly_fee = st.number_input("Monthly Service Fee (KSH):", 
                                     min_value=0,
                                     value=0)
    
    # Calculate
    if st.button("Generate Schedule"):
        schedule_df, summary_df = calculate_loan(
            loan_amount,
            months,
            monthly_rate,
            monthly_fee=monthly_fee
        )
        
        # Display Results
        st.subheader("Payment Schedule")
        st.dataframe(schedule_df)
        
        st.subheader("Summary")
        st.table(summary_df)
        
        # Visualization
        st.subheader("Payment Breakdown")
        fig = px.bar(schedule_df, 
                    x="Month", 
                    y=["Principal (KSH)", "Interest (KSH)", "Fees (KSH)"],
                    title="Monthly Payment Composition")
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()