from analysis import *
from database import *

def main():


    create_transactions_table()

    df = pd.read_csv("statement.csv",index_col=False)

    insert_transactions(df)

    df = get_all_transactions()

    cafe_transactions = get_cafe_transactions(df)
    
    print(f"Transactions: {get_transaction_count()}")
    print(f"Total spent: ${get_total_spending(cafe_transactions)}")
    print(f"Average spent: ${get_average_spending(cafe_transactions):.2f}", )
    

    print("\nMonthly Spending:\n")
    print(get_monthly_spending(cafe_transactions))

if __name__ == "__main__":
    main()

