import sqlite3 as db
import sys
from datetime import date

conn = db.connect('track.db')
cur = conn.cursor()

def create():
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses(
        id real primary key autoincrement, 
        amount real, 
        category text, 
        description text,
        date_of_expense date
    )''')
    conn.commit()


def commit_spend(amount, category, description=""):
    date_of_expense = date.today()
    cur.execute("INSERT INTO expenses VALUES (?,?,?,?)", (amount, category, description, date_of_expense))

def display_info():
    cur.execute("SELECT * FROM expenses")
    items = cur.fetchall()
    for item in items: 
        print(item)
    conn.commit()

def delete_transaction(id):
    cur.execute("DELETE FROM expenses WHERE id = ?", (id))
    conn.commit()

def menu(): 
    print("--------------")
    print("Menu.......")
    print("Type 'create' to reate database")
    print("Type 'commit' to log expense")
    print("Type 'info' to display all expenses")
    print("Tyep 'modify' to delete logs")
    print("Type 'exit' to quit")

if __name__ == '__main__':
    flag = True
    while(flag): 
        menu()
        user_input = input()
        if user_input == 'exit':
            flag = False
            conn.close()
            print("Database closed successfully")
        elif user_input == 'create':
            create()
            print("Log: Database successfully created.\n")
        elif user_input == 'commit':
            amount = input("What is the amount you would like to log?\n")
            if amount.isnumeric():
                category = input("What is the category of this transaction?\n")
                description = input("Would you like to add any descriptions?\n")
                commit_spend(amount, category, description)
                print("Log: Commit success.\n")
            else:
                print("Log: Amount must be a integer")
                print("Log: Commit failed")
        elif user_input == 'info':
            display_info()
            print("Log: Info display success.\n")
        elif user_input == 'modify': 
            id = input("What line would you like to delete?\n")
            if id.isnumeric(): 
                delete_transaction(int(id))
            else:
                print("Error: Invalid input of id, must be numeric")
        else:
            print("Error: Invalid option, please choose again.\n")

