from SimpleQIWI import *
from colorama import init, Fore
init()
G = Fore.GREEN
R = Fore.RED
B = Fore.BLUE
Y = Fore.YELLOW
M = Fore.MAGENTA
C = Fore.CYAN
col ='''
   ____ _ __    __ _ _        _              
  /___ (_) / /\ \ (_) |_ ___ | | _____ _ __  
 //  / / \ \/  \/ / | __/ _ \| |/ / _ \ '_ \ 
/ \_/ /| |\  /\  /| | || (_) |   <  __/ | | |
\___,_\|_| \/  \/ |_|\__\___/|_|\_\___|_| |_|
################(Version:2.0)################
|                  Author                   |
|           JTexas   and    Paris302        |
#############################################
'''
print (M,col,C)
def user_info():
	token=input('Token:')
	api = QApi(token=token, phone="")
	try:
		print(G,api.balance,C)
		pho=input('Mob:')
		com=input('Com:')
		def pay_info():
			try:	
				api.pay(account=pho, amount=input('Rub:'),comment=com)
			except:
				print(R,'Error:Money',C)
				return pay_info()
		pay_info()
		print(G,api.balance,C)
	except:
		print(R,'Error:Token',C)
		return user_info()
user_info()
input('Exit')
