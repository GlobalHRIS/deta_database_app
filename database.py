import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
DETA_KEY = "a0xtf7euf1h_iS7QUeEZh2TpeUnQ9B92NcRWxCgFU1uW"
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("employee_data1")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": Employee Number, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

