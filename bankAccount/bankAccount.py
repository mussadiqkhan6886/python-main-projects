def main():
    while Exception:
        try:
            balance = 120
            while True:
                print()
                user = int(input("Enter number to choose\n1. Show Balance \n2. Withdraw Money\n3. Deposit Money\n4. Exit\n\nCHOOSE:  "))
                if user == 1:
                    print(f"Your balance is {balance} USD")
                elif user == 2:
                    amount = int(input("Enter Amount of money You want to withdraw: "))
                    if amount < 0:
                        print("You Shall enter amount more than 0 please!!")
                    elif amount > balance:
                        print("NO INSUFFICENT FUNDS IN ACCOUNT SORRY ")
                    else:
                        balance -= amount
                        print(f"Your current balance is: {balance} USD")
                elif user == 3:
                    amount = int(input("Enter amount of money you want to deposit: "))
                    if amount < 0:
                        print("You shall deposit amount more than 0")
                    else:
                        balance += amount
                        print(f"Your current balance is: {balance} USD")
                elif user == 4:
                    print("BYEEE!!!")
                    break
        except ValueError:
            print("You shall enter Numbers please")
        if user == 4:
            break
        
main()