class Atm(object):

    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def check_balance(self):
        print("Checking balance")

    def deposit_cash(self):
        print("Depositing cash")

    def withraw_cash(self):
        print("Withrawing cash")
