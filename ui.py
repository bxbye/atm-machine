from classes.atm import Atm
atm = Atm()

while True:
    #If the ATM has no more bills or coins should try to use other quantities to allow the user to withdraw the amount.
    try:
        atm.display_content()
        amount = int(input("As a user\nI withdraw: "))
        if(amount == 0):
            print("Exit")
            break
        atm.withdraw(amount)
    except Exception as e:
        print("Error: ", str(e))