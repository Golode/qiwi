from SimpleQIWI import *

print "    _____  ________                                           "
print "   |     \|        \                                          "
print "    \$$$$$ \$$$$$$$$  ______   __    __   ______    _______   "
print "      | $$   | $$    /      \ |  \  /  \ |      \  /       \  "
print " __   | $$   | $$   |  $$$$$$\ \$$\/  $$  \$$$$$$\|  $$$$$$$  "
print "|  \  | $$   | $$   | $$    $$  >$$  $$  /      $$ \$$    \   "
print "| $$__| $$   | $$   | $$$$$$$$ /  $$$$\ |  $$$$$$$ _\$$$$$$\  "
print " \$$    $$   | $$    \$$     \|  $$ \$$\ \$$    $$|       $$  "
print "  \$$$$$$     \$$     \$$$$$$$ \$$   \$$  \$$$$$$$ \$$$$$$$   "
print "                           Ver:1.0                            "

api = QApi(token=raw_input('Api:'), phone="")
print(api.balance)

api.pay(account=raw_input('Pay:'), amount=raw_input('$:'))
print(api.balance)

exit = input("")


