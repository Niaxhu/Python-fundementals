

choice = int(input("Choose 1 to check balance, 2 to deposit, or 3 to withdraw: "))
#input() - asks the user to enter something, int() converts their input into an integer, choice - stores the number they entered

balance = 2000


if choice == 1:
    print(f"your balance is £{balance}")
    #f before the opening quotation mark to create an fstring, recognises balance as a variable and inserts its value
elif choice == 2:
     amount = float(input("How much would you like to deposit?:"))
     print((f"£{amount} deposited. New balance is £{balance +amount:}"))

elif choice == 3:
    amount = float(input("How much would you like to withdraw?:"))
    if amount > balance:
        print("insufficient funds")
    else:
        balance = balance - amount
        print(f"£{amount} withdrawn. New balance is £{balance}")
else:
    print("Invalid choice. Please try again.")


