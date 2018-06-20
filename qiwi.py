from SimpleQIWI import *
drower = raw_input('Api:')
api = QApi(token=drower, phone="")
print(api.balance)
api.pay(account=raw_input('Pay:'), amount=raw_input('$:'))
print(api.balance)
exit = raw_input("exit")

