# Stock Portfolio Tracker - Complete Implementation

portfolio = {}

def add_stock():
    name = input("Stock Name: ").upper()
    qty = int(input("Qty: "))
    buy = float(input("Buy Price: "))
    current = float(input("Current Price: "))
    portfolio[name] = {"qty": qty, "buy": buy, "current": current}
    print(f"{name} Added Successfully!")

def remove_stock():
    name = input("Remove cheyalsina Stock Name: ").upper()
    if name in portfolio:
        del portfolio[name]
        print(f"{name} Removed!")
    else:
        print("Stock not found!")

def update_price():
    name = input("Stock Name: ").upper()
    if name in portfolio:
        new_price = float(input("New Current Price: "))
        portfolio[name]["current"] = new_price
        print("Updated!")
    else:
        print("Stock not found!")

def show_portfolio():
    if not portfolio:
        print("Portfolio empty!")
        return
    invested = 0
    current = 0
    print("\n--- My Portfolio ---")
    for name, s in portfolio.items():
        inv = s["qty"] * s["buy"]
        cur = s["qty"] * s["current"]
        invested += inv
        current += cur
        print(f"{name} | Qty: {s['qty']} | Buy: {s['buy']} | Current: {s['current']} | Profit: {cur - inv}")
    
    profit = current - invested
    print(f"\nInvested: {invested} | Current: {current} | Profit: {profit} | Gain: {profit/invested*100:.2f}%")

# Main Menu
while True:
    print("\n1. Add Stock")
    print("2. Remove Stock")
    print("3. Update Price")
    print("4. Show Portfolio")
    print("5. Exit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        remove_stock()
    elif choice == "3":
        update_price()
    elif choice == "4":
        show_portfolio()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Wrong choice!")
