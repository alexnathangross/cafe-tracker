import pandas as pd

def get_cafe_transactions(df):
    targets = ["HC CAMPUS EATS", "HUNTER DELI", "HUNTER"]
    pattern = "|".join(targets) 
    cafe_transactions = df[df["description"].str.contains(pattern, case=False, na=False)]
    return cafe_transactions
   

def get_total_spending(cafe_transactions):
    total = cafe_transactions["amount"].abs().sum()
    return total

def get_transaction_count(cafe_transactions):
    return len(cafe_transactions)

def get_average_spending(cafe_transactions):
    if len(cafe_transactions) == 0:
        return 0
    else: 
        return cafe_transactions["amount"].abs().mean()
    
def get_monthly_spending(cafe_transactions):
    cafe_transactions = cafe_transactions.copy()
    cafe_transactions["posting_date"] = pd.to_datetime(cafe_transactions["posting_date"])

    monthly = cafe_transactions.groupby(cafe_transactions["posting_date"].dt.to_period("M"))["amount"].sum().abs()
    return monthly
    