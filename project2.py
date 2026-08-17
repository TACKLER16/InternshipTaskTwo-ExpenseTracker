def expense_tracker():
    total_spent = 0.0

    print("--- Expense Tracker ---")
    print("Enter your expense amounts one by one.")
    print("Type 'done' or '0' when you are finished.\n")

    while True:
        user_input = input("Enter expense amount: ").strip()

        if user_input.lower() == "done":
            break

        try:
            expense = float(user_input)

            if expense == 0:
                break
            elif expense < 0:
                print("Please enter a positive amount.")
                continue

            total_spent += expense
            print(f"Added ${expense:.2f}. Current total: ${total_spent:.2f}\n")

        except ValueError:
            print("Invalid input! Please enter a valid number or 'done'.\n")

    print("\n-----------------------")
    print(f"Total Spent: ${total_spent:.2f}")
    print("-----------------------")


if __name__ == "__main__":
    expense_tracker()
