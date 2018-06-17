from SimpleQIWI import *
drower = raw_input('Api:')
api = QApi(token=drower, phone="")
print(api.balance)
pay = raw_input('Pay:')
money = raw_input('$:')
api.pay(account=rpay, amount=money)
print(api.balance)
exit = input("")

