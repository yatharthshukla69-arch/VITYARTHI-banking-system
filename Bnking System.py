FILE = "bank_data.txt"

# -------------------------------
# Create Account
# -------------------------------
def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter account number: ")
    pin = input("Set 4-digit PIN: ")

    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.split(",")[0] == acc_no:
                    print("❌ Account already exists!")
                    return
    except FileNotFoundError:
        pass

    with open(FILE, "a") as f:
        f.write(f"{acc_no},{name},{pin},0\n")

    print("✅ Account created successfully!")


# -------------------------------
# Login System
# -------------------------------
def login():
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")

    try:
        with open(FILE, "r") as f:
            for line in f:
                a, name, p, balance = line.strip().split(",")
                if a == acc_no and p == pin:
                    print(f"✅ Welcome {name}!")
                    return acc_no
    except FileNotFoundError:
        pass

    print("❌ Invalid credentials!")
    return None


# -------------------------------
# Deposit
# -------------------------------
def deposit(acc_no):
    amount = float(input("Enter amount: "))
    updated = []

    with open(FILE, "r") as f:
        for line in f:
            a, name, pin, balance = line.strip().split(",")
            if a == acc_no:
                balance = str(float(balance) + amount)
            updated.append(f"{a},{name},{pin},{balance}\n")

    with open(FILE, "w") as f:
        f.writelines(updated)

    print("✅ Deposit successful!")


# -------------------------------
# Withdraw
# -------------------------------
def withdraw(acc_no):
    amount = float(input("Enter amount: "))
    updated = []

    with open(FILE, "r") as f:
        for line in f:
            a, name, pin, balance = line.strip().split(",")
            if a == acc_no:
                if float(balance) >= amount:
                    balance = str(float(balance) - amount)
                    print("✅ Withdrawal successful!")
                else:
                    print("❌ Insufficient balance!")
            updated.append(f"{a},{name},{pin},{balance}\n")

    with open(FILE, "w") as f:
        f.writelines(updated)


# -------------------------------
# Check Balance
# -------------------------------
def check_balance(acc_no):
    with open(FILE, "r") as f:
        for line in f:
            a, name, pin, balance = line.strip().split(",")
            if a == acc_no:
                print(f"💰 Balance: ₹{balance}")


# -------------------------------
# Transfer Money
# -------------------------------
def transfer_money(acc_no):
    target = input("Enter receiver account number: ")
    amount = float(input("Enter amount: "))

    updated = []
    found_target = False

    with open(FILE, "r") as f:
        data = f.readlines()

    for line in data:
        a, name, pin, balance = line.strip().split(",")

        if a == acc_no:
            if float(balance) >= amount:
                balance = str(float(balance) - amount)
            else:
                print("❌ Insufficient balance!")
                return

        if a == target:
            balance = str(float(balance) + amount)
            found_target = True

        updated.append(f"{a},{name},{pin},{balance}\n")

    if not found_target:
        print("❌ Target account not found!")
        return

    with open(FILE, "w") as f:
        f.writelines(updated)

    print("✅ Transfer successful!")


# -------------------------------
# User Menu
# -------------------------------
def user_menu(acc_no):
    while True:
        print("\n------ Banking Menu ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            deposit(acc_no)
        elif choice == '2':
            withdraw(acc_no)
        elif choice == '3':
            check_balance(acc_no)
        elif choice == '4':
            transfer_money(acc_no)
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice!")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n====== REAL BANKING SYSTEM ======")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            acc_no = login()
            if acc_no:
                user_menu(acc_no)
        elif choice == '3':
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice!")


# Run
if __name__ == "__main__":
    main()