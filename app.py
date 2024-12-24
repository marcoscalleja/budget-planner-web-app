import streamlit as st
from components.user_auth import login, register
from components.budget_management import manage_budgets
from components.expense_tracking import track_expenses
from components.data_visualization import display_insights

st.set_page_config(page_title="Buddy: Budget Planner", layout="wide")

# Sidebar Navigation
st.sidebar.title("Buddy: Budget Planner")
menu = st.sidebar.selectbox("Navigate", ["Home", "Login", "Register", "Budgets", "Expenses", "Insights"])

# Main Pages
if menu == "Home":
    st.title("Welcome to Buddy: Budget Planner")
    st.image("assets/logo.png", width=200)
    st.write("""
    Plan, track, and manage your finances with ease!
    Use the navigation menu to get started.
    """)

elif menu == "Login":
    login()

elif menu == "Register":
    register()

elif menu == "Budgets":
    manage_budgets()

elif menu == "Expenses":
    track_expenses()

elif menu == "Insights":
    display_insights()
